import pickle as pkl
from pathlib import Path
import sys

query = sys.stdin.read()

def highlights_to_roamStyle(h):
    highlights = ""
    for i in h:
        highlights += '- ' + i['chapterName'] + '\n'
        for c in i['chapterNotes']:
            highlights += '  - ' + c + '\n'
    return highlights


def deal_highlight(string):
    highlights = [i.strip('\\n').strip() for i in string.split('>>>')]
    chapter_notes = {
        'chapterName': "",
        'chapterNotes': []
    }
    chapters = []
    bookName = ''
    for i in highlights:
        if i.startswith('#title'):
            if len(chapter_notes['chapterNotes']) != 0:
                chapters.append(chapter_notes)
            chapter_notes = {}
            chapter_notes['chapterName'] = i.strip('#title').strip()
            chapter_notes['chapterNotes'] = []
        elif i.startswith('#highlight'):
            chapter_notes['chapterNotes'].append(i.strip('#highlight').strip())
        elif i.startswith('#fleeting'):
            chapter_notes['chapterNotes'][-1] += '\n    - ' + i.strip('#fleeting').strip()
        elif i.startswith('#bookName'):
            bookName = i.strip('#bookName').strip()
        else:
            continue
    chapters.append(chapter_notes)
    if Path(f'./save_{bookName}.pkl').exists():
        saved_highlights = pkl.load(Path(f'./save_{bookName}.pkl').open('rb'))
        saved_chapters = [i['chapterName'] for i in saved_highlights]
        now_chapters = [i['chapterName'] for i in chapters]
        need_export = []
        for index, chapterName in enumerate(now_chapters):
            if chapterName not in saved_chapters:
                need_export.append(chapters[index])
                continue
            saved_h = saved_highlights[saved_chapters.index(chapterName)]['chapterNotes']
            now_highlights = [i for i in chapters[index]['chapterNotes'] if i not in saved_h]
            if len(now_highlights) == 0:
                continue
            need_export.append({
                'chapterName': chapterName,
                'chapterNotes': now_highlights
            })
        with open(f'./save_{bookName}.pkl', 'wb') as f:
            pkl.dump(chapters, f)
        return highlights_to_roamStyle(need_export)
    else:
        with open(f'./save_{bookName}.pkl', 'wb') as f:
            pkl.dump(chapters, f)
        return highlights_to_roamStyle(chapters)

            

print(deal_highlight(query))
    
