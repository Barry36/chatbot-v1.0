APP = ['tmp.py']
DATA_FILES = ['intents_CN.json']
OPTIONS = {
 'iconfile':'logoapp.icns',
 'argv_emulation': True,
 'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)