# medical-document-ocr-extraction
OCR and information extraction pipeline for synthetic medical documents.
# Medical Document OCR & Information Extraction

## Project context

Hospitals often store medical documents as scanned PDFs or images. These documents are difficult to exploit automatically because the information is not directly available as structured data.

This project simulates a local OCR pipeline for extracting structured information from synthetic medical documents.

## Objective

The objective is to build a small end-to-end pipeline that can:

- generate synthetic medical documents;
- convert them into scanned-like images;
- preprocess images before OCR;
- extract text using OCR engines;
- extract structured information from OCR text;
- evaluate the quality of the extraction.

## Important note

This project uses only synthetic medical documents.  
No real patient data is used.

## Tools planned

- Python
- OpenCV
- Tesseract OCR
- EasyOCR
- pandas
- regex
- spaCy

## Project status

Day 1: repository creation and project structure.
