"""Retrieval-Augmented Generation engine for sustainability knowledge base."""

from __future__ import annotations

import re
from pathlib import Path
from typing import NamedTuple

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class DocumentChunk(NamedTuple):
    source: str
    text: str


class RAGEngine:
    """TF-IDF based RAG engine — lightweight, no GPU required."""

    def __init__(self, knowledge_dir: Path):
        self.knowledge_dir = knowledge_dir
        self.chunks: list[DocumentChunk] = []
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            max_features=5000,
        )
        self.matrix = None
        self._load_and_index()

    def _load_and_index(self) -> None:
        for file_path in sorted(self.knowledge_dir.glob("*.txt")):
            content = file_path.read_text(encoding="utf-8")
            sections = re.split(r"\n(?=[A-Z][A-Z\s/&-]+:|\n)", content)
            for section in sections:
                section = section.strip()
                if len(section) > 40:
                    self.chunks.append(DocumentChunk(source=file_path.stem, text=section))

        if not self.chunks:
            raise ValueError(f"No knowledge chunks found in {self.knowledge_dir}")

        corpus = [c.text for c in self.chunks]
        self.matrix = self.vectorizer.fit_transform(corpus)

    def retrieve(self, query: str, top_k: int = 4) -> list[DocumentChunk]:
        if not query.strip():
            return self.chunks[:top_k]

        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.matrix).flatten()
        top_indices = np.argsort(scores)[::-1][:top_k]
        return [self.chunks[i] for i in top_indices if scores[i] > 0]

    def format_context(self, chunks: list[DocumentChunk]) -> str:
        if not chunks:
            return "No specific context found."
        parts = []
        for i, chunk in enumerate(chunks, 1):
            parts.append(f"[Source: {chunk.source}]\n{chunk.text}")
        return "\n\n---\n\n".join(parts)

    def answer_question(self, question: str) -> dict:
        chunks = self.retrieve(question)
        context = self.format_context(chunks)

        answer = self._generate_answer(question, context, chunks)
        return {
            "answer": answer,
            "sources": list({c.source for c in chunks}),
            "context_preview": context[:500] + "..." if len(context) > 500 else context,
        }

    def _generate_answer(self, question: str, context: str, chunks: list[DocumentChunk]) -> str:
        """Rule-based answer generation using retrieved context."""
        q = question.lower()
        lines = []

        if any(w in q for w in ["waste", "bin", "segregat", "recycl", "plastic", "compost"]):
            lines.append("**Waste & Segregation Guidance**")
            for chunk in chunks:
                if "waste" in chunk.source or "segregat" in chunk.text.lower():
                    lines.extend(self._extract_bullets(chunk.text, max_items=5))

        elif any(w in q for w in ["water", "shower", "tap", "drought", "rain"]):
            lines.append("**Water Conservation Guidance**")
            for chunk in chunks:
                if "water" in chunk.source or "water" in chunk.text.lower():
                    lines.extend(self._extract_bullets(chunk.text, max_items=5))

        elif any(w in q for w in ["carbon", "co2", "emission", "climate", "transport", "footprint"]):
            lines.append("**Carbon Footprint Guidance**")
            for chunk in chunks:
                if "carbon" in chunk.source or "co2" in chunk.text.lower():
                    lines.extend(self._extract_bullets(chunk.text, max_items=5))

        else:
            lines.append("**Sustainability Guidance**")
            for chunk in chunks[:2]:
                lines.extend(self._extract_bullets(chunk.text, max_items=3))

        if not lines or len(lines) == 1:
            lines.extend(self._extract_bullets(chunks[0].text if chunks else context, max_items=4))

        lines.append("\n**Action for today:** Pick one tip above and practice it on campus.")
        lines.append(
            "\n*Note: This guidance is AI-assisted and based on campus sustainability "
            "best practices. Verify local municipal rules when in doubt.*"
        )
        return "\n".join(lines)

    @staticmethod
    def _extract_bullets(text: str, max_items: int = 5) -> list[str]:
        bullets = []
        for line in text.split("\n"):
            line = line.strip()
            if line.startswith("-") or line.startswith("•"):
                bullets.append(line)
            elif re.match(r"^\d+\.", line):
                bullets.append(f"- {line[line.index('.')+1:].strip()}")
            if len(bullets) >= max_items:
                break
        if not bullets:
            sentences = [s.strip() for s in re.split(r"[.!?]", text) if len(s.strip()) > 20]
            bullets = [f"- {s}." for s in sentences[:max_items]]
        return bullets
