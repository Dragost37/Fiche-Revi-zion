from pathlib import Path
import re


def fix_single_backtick_text_blocks(p: Path) -> bool:
    text = p.read_text(encoding="utf-8", errors="replace")
    # Replace blocks of the form:
    # `\text\n...\n`
    pattern = re.compile(r"(?ms)^`\\text\s*\r?\n(.*?)\r?\n^`\s*$")
    new_text, n = pattern.subn(r"```text\n\1\n```", text)
    if n:
        p.write_text(new_text, encoding="utf-8")
        return True
    return False


def main():
    root = Path.cwd()
    total = 0
    for md in root.glob("*.md"):
        if fix_single_backtick_text_blocks(md):
            print(f"Fixed code fences in {md}")
            total += 1
    print(f"Done. {total} file(s) updated.")


if __name__ == "__main__":
    main()
