from pathlib import Path


def fix_file(p: Path) -> bool:
    text = p.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("`"):
            print(f"candidate line {i+1}: {repr(s)}")
        if (s.startswith("`") and s[1:].strip().lower() in {"text", "ext"}):
            print('DEBUG startswith matched at line', i+1)
            # find closing line with just a backtick
            j = i + 1
            while j < len(lines) and lines[j].strip() != "`":
                j += 1
            if j < len(lines):
                block = lines[i+1:j]
                print(f"Found block in {p} from {i+1} to {j+1} with {len(block)} lines")
                new_lines = lines[:i] + ["```text"] + block + ["```"] + lines[j+1:]
                p.write_text("\n".join(new_lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")
                return True
    return False


def main():
    # target the fiche file
    candidates = list(Path('.').glob('Fiche*md'))
    if not candidates:
        print('No target .md file found')
        return
    p = candidates[0]
    changed = fix_file(p)
    print('Changed' if changed else 'No changes')


if __name__ == '__main__':
    main()


