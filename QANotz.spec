# -*- mode: python ; coding: utf-8 -*-
import os
import sys

block_cipher = None
# This ensures we get the absolute path to your project root
project_root = os.path.abspath(os.getcwd())

a = Analysis(
    ['main.py'],
    pathex=[project_root],
    binaries=[],
    # This force-adds the entire folder into the bundle
    datas=[('qanotz', 'qanotz')], 
    hiddenimports=[
        'qanotz',
        'qanotz.data',
        'qanotz.data.data',
        'qanotz.ui',
        'qanotz.ui.ui',
        'qanotz.utils'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='QANotz',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['QANotz.ico' if os.path.exists('QANotz.ico') else None],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='QANotz',
)

app = BUNDLE(
    coll,
    name='QANotz.app',
    icon='QANotz.icns' if os.path.exists('QANotz.icns') else None,
    bundle_identifier='com.qanotz.app',
)