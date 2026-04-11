# arxiv-llm-daily

a daily digest of fresh [arxiv](https://arxiv.org) papers in `cs.CL` and `cs.AI`,
committed to git.

the LLM space moves fast. the git history of this repo is the slowest possible
newsletter: one commit per day, one file per day, no algorithm deciding what you
should read. just yesterday's papers, stitched to their abstracts and authors,
archived forever.

## how it works

a [github actions workflow](.github/workflows/scrape.yml) runs once a day,
queries the [arxiv public API](https://info.arxiv.org/help/api/index.html) for
new submissions in `cs.CL` and `cs.AI`, filters to the last 36 hours, and writes
a dated markdown file to `papers/`.

no key, no auth, no babysitting.

## browse

- [`latest.md`](./latest.md) — yesterday's digest
- [`papers/YYYY-MM-DD.md`](./papers) — the full archive

## credits

arxiv provides metadata under [CC0](https://arxiv.org/help/license/index) and
abstracts under licenses that generally permit non-commercial reuse. this repo
mirrors only titles, authors, abstracts, and links for archival and research
purposes. all papers are the property of their respective authors.
