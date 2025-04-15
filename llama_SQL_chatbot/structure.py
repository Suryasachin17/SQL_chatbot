import os


project_structure = {
    "async_chatbot_project":[
        "main.py",
        "config.py",
        "requirement.txt",
        {"services": ["database_service.py", "ollama_service.py", "prompt_service.py"]},
        {"utils": ["sql_saniotizer.py"]},
        {"logs": ["chatbot.log"]}
    ]
}




def project_struc(project,dir = "."):
    for name,content in project.items():
        project_path = os.path.join(dir,name)
        os.makedirs(project_path,exist_ok=True)
        
        for  files in content:
            if isinstance(files,dict):
                project_struc(files,dir = project_path)
            else:
                file_path = os.path.join(project_path,files)
                with open(file_path, 'w') as f:
                    template = files
                    f.write(template)
            print(files,"98764123")
        
        
        
        
        
        
        
        
        
        
        
        
project =    project_structure     
project_struc(project_structure)        
        
        
        
        
        
        
        