# -*- mode: python -*-

block_cipher = None


a = Analysis(['naver.py'],
             pathex=['F:\\sublime\\���μ���-shin-����ftp\\�������α׷�\\naver_analytics'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='naver',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
