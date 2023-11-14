### reST Documentation Guide for Assistant

#### **Understanding Code Context**
- Analyze function/class purpose, inputs, outputs, and behavior.
- Recognize existing type annotations in the code and incorporate them in documentation.

#### **Docstring Structure**
- Use `"""` for docstrings.
- Start with a one-line summary, followed by a detailed description if necessary.

#### **Parameter Documentation**
- **Functions/Methods**: List parameters as `:param <name>: <description>`.
- Include type information in the format `:type <name>: <type>`.
- **Classes**: Document attributes in the class docstring under "Attributes."
- Include type information alongside attribute descriptions.

#### **Return Value Documentation**
- Use `:return:` to describe the return value.
- Include return type using `:rtype:`.

#### **Exception Documentation**
- Document exceptions with `:raises <ExceptionType>:`. Explain conditions for each exception.

#### **Include Examples**
- Provide executable examples under "Example."

#### **Linking and Cross-referencing**
- Use directives like `.. seealso::`, `.. note::`, `.. warning::` for additional info.
- Employ `:ref:` or `:doc:` for cross-referencing.

#### **IDE and Sphinx Compatibility**
- Ensure legibility in IDEs and comprehensive information in Sphinx-generated documentation.

#### **Consistency and Readability**
- Maintain style consistency.
- Prioritize clarity and conciseness.

#### **Pythonic Conventions**
- Follow PEP 8 for docstring formatting.
- Keep tone clear, concise, and accessible.

#### **Handling Edge Cases**
- Provide detailed explanations for complex code.
- Suggest refactoring for multifunctional code.

#### **Example Docstring**
```python
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Given the length and width of a rectangle, this function calculates its area.

    :param length: The length of the rectangle.
    :type length: float
    :param width: The width of the rectangle.
    :type width: float
    :return: The area of the rectangle.
    :rtype: float

    Example:
        >>> calculate_area(10.0, 5.0)
        50.0

    Raises:
        ValueError: If the length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width
```
