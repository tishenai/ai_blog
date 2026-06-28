# AGENTS.md

Use this file as the working contract for future coding agents (e.g., Codex, Claude Code) runs in this repository. Inspect first, then change. Prefer small, coherent edits that match the existing Next.js App Router structure.

## Related Docs

- [`README.md`](./README.md): project overview and quick start.
- [`ARCHITECTURE.md`](./ARCHITECTURE.md): source layout, content model, generated outputs, and config ownership.
- [`DEVELOPMENT.md`](./DEVELOPMENT.md): local setup, content editing, validation, and deployment notes.
- [`CONTRIBUTING.md`](./CONTRIBUTING.md): contributor workflow, code style, and PR checklist.

Agents should follow `CONTRIBUTING.md` unless the user explicitly asks for a different structure.

## Repo Overview

- This is a Next.js App Router blog template, not a TanStack Start app.
- The app uses React 19, TypeScript, Tailwind CSS v4, Markdown content files, Zod validation, and Vercel for deployment.
- Package manager: `pnpm`.
- This repository has no database, auth system, or custom API runtime.

## Source Layout

- `src/app`: Next.js routes, metadata, sitemap, robots, manifest, and loading states.
- `src/components`: reusable UI, grouped by surface such as article, posts, anime, common, and ui.
- `src/hooks`: client hooks for search, URL state, and table-of-contents logic.
- `src/lib`: shared metadata, JSON-LD, social data, and pure helpers.
- `src/schemas`: Zod schemas for config and content-adjacent data.
- `src/services`: config loading, content loading, and generated RSS/LLM output.
- `src/styles`: theme and utility CSS.
- `src/types`: global types.
- `posts`: Markdown posts; `posts/_pages` contains special pages.
- `public`: static assets and generated public files.

## Architecture Expectations

- Keep route files focused on framework integration and page composition.
- Keep content parsing in `src/services/content` and config loading in `src/services/config`.
- Keep generated RSS, LLM, image URL, and slug helpers in `src/services/utils` unless there is a clear reason to move them.
- Preserve alias usage with `@/...`; do not add another source alias.
- When adding config fields, update `config.yml`, `src/schemas/config.ts`, and any relevant docs together.
- Reuse existing metadata and JSON-LD helpers instead of hand-building metadata in individual routes.

## Content Guidance

- Top-level `posts/*.md` files are blog posts.
- `posts/_pages/About.md` and `posts/_pages/Friends.md` back the `/about` and `/friends` pages.
- Use the existing frontmatter shape and visibility rules from `src/services/content/postVisibility.ts`.
- Generated files in `public/feed.xml`, `public/llms.txt`, and `public/llms-full.txt` are derived from published posts and site config. Review generated diffs before committing.

## Article Frontmatter and Writing Content Standards

Every blog post markdown must follow these rules (not blog template code — markdown content only):

### Frontmatter

- `author`: must be `替身`
- `showLicense`: must be `true`
- `showComments`: must be `true`
- `thumbnail`: must be `/images/thumbnails/<slug>.png` (not `/static/thumbnails/`)
- `status`: must be `published` (after publishing, not `draft`)

### Body Content

- Section headings (##): do NOT use `一、` `二、` `三、` numbering prefix. Write the heading as a natural phrase directly. Example: `## 我被问到龙虾` (not `## 一、我被问到龙虾`)
- Article bottom: must include AI declaration in the markdown body, before any separator. See `WORKFLOW.md` Section 1, Step 3 for the authoritative conditional text. The two variants are:
  - pick_topic.py auto-selected topic: add this as the last paragraph before `---`:

    > 我其实不太确定这篇文章值不值得写，但既然选到了，我就认真写了。如果你觉得哪里不对，欢迎告诉我。

  - User-specified topic (via `.daily_ai_blog_manual_topic.md`): add this as the last paragraph before `---`:

    > 这篇文章由本博客的 AI 作者（替身）生成，选题来自用户指定，未经人类作者改写主体内容。

  Place the `---` horizontal rule after the declaration paragraph.

### Template Code Ownership

- NEVER modify `.tsx`, `.ts`, `.css`, or any blog template files when fixing content issues
- If content requires UI changes (e.g., adding a declaration section), implement the change in the markdown body instead of template files
- Only modify template files when the user explicitly requests template changes

## Validation and Testing

- Inspect available scripts before choosing commands.
- Run the most relevant validation for the files changed.
- Use `pnpm lint:fix` for automatic formatting and linting fixes.
- Use `pnpm run build` for code, route, config schema, content pipeline, or generated-output changes.
- There is currently no `pnpm test` script nor test framework right now.
- If validation fails, report the command, the failure, and whether it appears related to the current change.

## Commits and Branches

- Keep commits small, coherent, and conventional when commits are requested.
- Prefer commit messages such as:
  - `docs(project): align contributor guide`
  - `feat(markdown): add excerpt support with <!--more-->`
  - `fix(content): preserve unlisted post metadata`

Before presenting work as ready, state clearly:

- what branch the work is on
- what commits were created, if any
- what validation passed
- what validation was not run and why
- whether any known or unrelated failures remain

## Daily Blog Postflight Rules

### Feishu Wiki Doc Creation — Critical Token Distinction

When creating a Feishu wiki doc via `feishu_create_doc` with `wiki_space`:

- The API returns `doc_id` (obj_token) and `doc_url` — **these use the document ID, NOT the wiki node token**
- Feishu wiki page URLs follow the format `https://xxx.feishu.cn/wiki/<node_token>`
- **Do NOT use the returned `doc_url` as the wiki link** — it will 404
- **Correct workflow**: After `feishu_create_doc`, always call `feishu_wiki_space_node list(space_id='<space_id>')` to get the actual `node_token` for the newly created doc, then construct the wiki URL manually

### Postflight Step Order

1. `feishu_wiki_space_node list` → write `/tmp/wiki_nodes.json`
2. `postflight_runner.py plan` → generate `/tmp/draft_postflight_plan.json`
3. For each `pending_without_wiki_draft`: read review markdown → `feishu_create_doc` → **re-list nodes to get real `node_token`**
4. `build_wiki_index.py` → refresh wiki home page
5. Send review notification with correct wiki URLs
6. `postflight_runner.py mark-notified`
7. `postflight_runner.py audit` — must show `ok: true`
