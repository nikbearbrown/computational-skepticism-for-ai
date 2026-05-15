#!/bin/bash
set -e

BOOK_SLUG="book"
METADATA="metadata.yaml"
OUTPUT_DIR="output"

mkdir -p "$OUTPUT_DIR"

# Compile chapters in filename order
# 00-frontmatter → 00-introduction → 02..NN chapters → 99-back-matter
cat $METADATA chapters/*.md > "$OUTPUT_DIR/combined.md"

# EPUB (primary — upload this to KDP)
pandoc "$OUTPUT_DIR/combined.md" \
  --from markdown-implicit_figures \
  --mathml \
  --to epub3 \
  --epub-cover-image=cover.jpg \
  --css=styles/kindle.css \
  --css=styles/kindle-book.css \
  --toc --toc-depth=2 \
  --output="$OUTPUT_DIR/$BOOK_SLUG.epub"

# HTML (proofing — mirrors EPUB cascade exactly)
pandoc "$OUTPUT_DIR/combined.md" \
  --from markdown-implicit_figures \
  --mathml \
  --to html5 \
  --standalone \
  --css=styles/kindle.css \
  --css=styles/kindle-book.css \
  --toc \
  --output="$OUTPUT_DIR/$BOOK_SLUG.html"

echo "Built: $OUTPUT_DIR/$BOOK_SLUG.epub"
echo "Built: $OUTPUT_DIR/$BOOK_SLUG.html"
