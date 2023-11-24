import os

for root, dirs, files in os.walk('src'):
    if '__pycache__' not in root:
        init_path = os.path.join(root, '__init__.py')
        if not os.path.exists(init_path):
            open(init_path, 'a').close()