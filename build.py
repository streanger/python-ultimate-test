from pathlib import Path
import re

def to_code_html(text):
    return re.sub(r'`([^`]+)`', r'<code class="bg-light px-1 rounded">\1</code>', text)

# create new body
item = """\
              <tr>
                <td>{question}</td>
                <td class="answer-cell">
                  <input type="radio" class="btn-check" name="{name}" id="{name}-yes" value="yes" required autocomplete="off">
                  <label class="btn btn-choice btn-yes" for="{name}-yes">Yes</label>
                  <input type="radio" class="btn-check" name="{name}" id="{name}-no" value="no" autocomplete="off">
                  <label class="btn btn-choice btn-no" for="{name}-no">No</label>
                </td>
              </tr>\
"""
questions = [q for q in Path('questions.txt').read_text().splitlines() if q.strip()]
body_rows = []
for index, question in enumerate(questions, start=1):
    question = to_code_html(question)
    row = item.format(question=f'{index}. {question}', name=f"q{index}")
    body_rows.append(row)

body = '\n'.join(body_rows)

# replace old html with new one
index_file = 'index.html'
old_html = Path(index_file).read_text()
tbody_begin_pattern = '<tbody>'
tbody_end_pattern = '</tbody>'
tbody_begin = old_html.find(tbody_begin_pattern) + len(tbody_begin_pattern)
tbody_end = old_html.find(tbody_end_pattern) - 10  # whitespaces
new_html = f'{old_html[:tbody_begin]}\n{body}\n{old_html[tbody_end:]}'
Path(index_file).write_text(new_html)
print(f'{index_file} updated')
