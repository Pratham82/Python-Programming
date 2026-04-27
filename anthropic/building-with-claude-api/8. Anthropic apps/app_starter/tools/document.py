from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pathlib import Path
from pydantic import Field

SUPPORTED_EXTENSIONS = {".pdf", ".docx"}


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    path: str = Field(description="Absolute or relative path to a PDF or DOCX file"),
) -> str:
    """Convert a PDF or DOCX file at the given path to markdown-formatted text.

    Reads the file from disk, converts its contents to markdown, and returns
    the result as a string. Supports .pdf and .docx file types only.

    When to use:
    - When you have a local file path and need its contents as markdown
    - When processing documents for text extraction or summarization

    Examples:
    >>> document_path_to_markdown("/docs/report.pdf")
    "# Report Title\\n\\nContent..."
    >>> document_path_to_markdown("/docs/notes.docx")
    "# Notes\\n\\n- Item one..."
    """
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"No file found at path: {path}")

    ext = file_path.suffix.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type '{ext}'. Must be one of: {', '.join(SUPPORTED_EXTENSIONS)}"
        )

    binary_data = file_path.read_bytes()
    return binary_document_to_markdown(binary_data, ext.lstrip("."))
