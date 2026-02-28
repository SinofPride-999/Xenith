# Xenith Language Support

Xenith is a modern C-like programming language designed for simplicity and clarity.

This extension provides syntax highlighting support for `.xen` files in Visual Studio Code.

---

## Features

- Syntax highlighting for:
  - Keywords (`VAR`, `FUN`, `IF`, `ELSE`, `FOR`, etc.)
  - Built-in functions (`PRINT`, `LEN`, `IS_NUM`, etc.)
  - Types (`INT`, `FLOAT`, `STRING`, etc.)
  - Numbers and strings
  - Comments using `#`
  - List operations (`APPEND`, `POP`, `/`)
- Automatic `.xen` file recognition

---

## Usage

Create a file with the `.xen` extension:

```xen
# Example Xenith program

VAR x = 10

FUN add(a, b) {
    RETURN a + b
}

PRINT(add(x, 5))
```
