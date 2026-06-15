#!/usr/bin/env bash
cd "$(dirname "$0")"

echo ""
echo "  ========================================"
echo "   EcoGuide AI - Campus Sustainability"
echo "   Starting global server on port 8501..."
echo "  ========================================"
echo ""
echo "   Local:    http://localhost:8501"
echo "   Network:  http://$(hostname -I 2>/dev/null | awk '{print $1}'):8501"
echo ""
echo "   Press Ctrl+C to stop the server."
echo ""

python3 -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
