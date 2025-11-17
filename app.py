from flask import Flask, render_template, url_for
import os
import markdown

app = Flask(__name__)

# Configuration
app.config['CONTENT_FOLDER'] = 'Chapter-1-Recursive-Modelling'

@app.route('/')
def index():
    # Get all markdown files in the content folder
    content_dir = os.path.join(app.root_path, app.config['CONTENT_FOLDER'])
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    
    # Sort files based on the number prefix
    files.sort(key=lambda x: int(x.split('.')[0]) if x.split('.')[0].isdigit() else float('inf'))
    
    # Prepare file data with titles
    chapters = []
    for file in files:
        with open(os.path.join(content_dir, file), 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            # Remove markdown heading syntax if present
            title = first_line.lstrip('# ').strip() if first_line.startswith('#') else file
            chapters.append({
                'file': file,
                'title': title,
                'url': url_for('show_chapter', filename=file)
            })
    
    return render_template('index.html', chapters=chapters)

@app.route('/chapter/<filename>')
def show_chapter(filename):
    filepath = os.path.join(app.root_path, app.config['CONTENT_FOLDER'], filename)
    
    if not os.path.exists(filepath):
        return "Chapter not found", 404
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        html_content = markdown.markdown(content, extensions=['fenced_code', 'tables', 'codehilite'])
    
    return render_template('chapter.html', content=html_content, title=filename)

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    app.run(debug=True)
