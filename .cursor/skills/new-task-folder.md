# Skill: Create a folder for each new task

## When to use

Use this skill **every time** the user asks for a completely new task, meaning a task that is NOT a follow-up, continuation, or refinement of a previous task in the same conversation.

### What counts as a "new task"

- The user's request introduces a distinct goal unrelated to prior work in the conversation.
- The user explicitly says "new task," "new project," "start fresh," or similar phrasing.
- The first message in a conversation is always considered a new task.

### What does NOT count as a "new task"

- A follow-up that refines, extends, or iterates on the previous task (e.g., "now add tests for that," "fix the bug we just discussed," "also update the styles").
- A clarification or correction of the current task.

## Procedure

1. **Choose a folder name.** Derive a short, descriptive `snake_case` name from the task description. For example, if the user says "Build me a REST API for managing todos," the folder name should be something like `todo_rest_api`.

2. **Create the folder** at the repository root:
   ```
   /workspace/<task_folder_name>/
   ```

3. **Inform the user** that you created the folder and will place all task-related files inside it.

4. **Place all files for that task inside the folder.** Any source code, configs, tests, or documentation produced for the task should live under this folder unless the user specifies otherwise.

## Examples

| User request | New task? | Action |
|---|---|---|
| "Create a Python CLI that converts CSV to JSON" | Yes | Create `/workspace/csv_to_json_cli/` |
| "Now add a `--pretty` flag to it" | No (follow-up) | Continue working in the existing folder |
| "Build a React dashboard for analytics" | Yes | Create `/workspace/analytics_dashboard/` |
| "Fix the chart colors" | No (follow-up) | Continue in `/workspace/analytics_dashboard/` |
| "New task: set up a PostgreSQL schema for users" | Yes | Create `/workspace/user_pg_schema/` |
