def chunk_to_text(chunk):
    parts = []

    # Symbol type
    parts.append(f"Symbol Type: {chunk['type'].replace('_', ' ').title()}")

    # Symbol name
    parts.append(f"Name: {chunk['name']}")

    # Full qualified name
    parts.append(f"Qualified Name: {chunk['qualified_name']}")

    # Class
    if chunk.get("class_name"):
        parts.append(f"Belongs to Class: {chunk['class_name']}")

    # File
    parts.append(f"Defined In: {chunk['file']}")

    # Location
    if chunk.get("lineno"):
        if chunk.get("end_lineno"):
            parts.append(
                f"Lines: {chunk['lineno']}-{chunk['end_lineno']}"
            )
        else:
            parts.append(f"Line: {chunk['lineno']}")

    # Parameters
    if chunk.get("args"):
        parts.append(
            "Function Parameters: "
            + ", ".join(chunk["args"])
        )

    # Documentation
    if chunk.get("docstring"):
        parts.append(
            "Documentation:\n"
            + chunk["docstring"].strip()
        )

    # Relationships
    if chunk.get("calls"):
        parts.append(
            "Calls These Functions:\n"
            + ", ".join(chunk["calls"])
        )

    # Source code
    if chunk.get("source"):
        parts.append(
            "Python Source Code:\n"
            + chunk["source"]
        )

    return "\n\n".join(parts)
