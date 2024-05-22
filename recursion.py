import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)


task_hierarchy_1 = [
    {
        "name": "Project",
        "subtasks": [
            {"name": "Define project scope"},
            {"name": "Create project plan"},
            {"name": "Assign project team",
            "subtasks": [
                {"name": "Identify team members"},
                {"name": "Allocate roles and responsibilities"}
            ]},
            {"name": "Conduct project kickoff meeting"}
        ]
    },
    {
        "name": "Research",
        "subtasks": [
            {"name": "Gather data"},
            {"name": "Analyze data",
            "subtasks": [
                {"name": "Data cleaning"},
                {"name": "Statistical analysis"}
            ]},
            {"name": "Draw conclusions"}
        ]
    }
]

task_hierarchy_2 = [
    {
        "name": "Homework",
        "subtasks": [
            {"name": "Math assignment",
            "subtasks": [
                {"name": "Complete worksheet"},
                {"name": "Study for quiz"}
            ]},
            {"name": "History essay",
            "subtasks": [
                {"name": "Research topic"},
                {"name": "Write essay"}
            ]}
        ]
    },
    {
        "name": "Home project",
        "subtasks": [
            {"name": "Garden renovation",
            "subtasks": [
                {"name": "Design garden layout"},
                {"name": "Purchase plants and materials"}
            ]},
            {"name": "DIY furniture",
            "subtasks": [
                {"name": "Select furniture design"},
                {"name": "Buy materials"},
                {"name": "Assemble furniture"}
            ]}
        ]
    }
]
    

def list_tasks(task_hierarchy, key):
    for i in task_hierarchy:
        if isinstance(i, dict):
            print(f'{key}: {i['name']}')
            if 'subtasks' in i:
                list_tasks(i['subtasks'], 'SUBTASKS')


list_tasks(task_hierarchy_1, 'TASKS')
line_break()
list_tasks(task_hierarchy_2, 'TASKS')
