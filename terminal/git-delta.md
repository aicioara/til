# Git Delta

Today I found an amazing tool called [git-delta](https://github.com/dandavison/delta). This improves the way your diffs look like, adding syntax highlighting and word-level diffs.

### Install

```bash
brew install git-delta
```

### Usage

```bash
git diff | delta
```

### Git integration

```
[core]
    pager = delta --plus-color="#012800" --minus-color="#340001"

[interactive]
    diffFilter = delta --color-only
````
