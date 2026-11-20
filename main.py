#!/usr/bin/env python3
"""Copy the rendered front page into the grader's output directory.

The source image is resolved from this file's own location, never from
the process working directory. The output directory is created if
needed and its existing contents are left alone -- in the grader
/output is a mount point, so it must never be removed.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("copied", src, "->", dst)


if __name__ == "__main__":
    main()
