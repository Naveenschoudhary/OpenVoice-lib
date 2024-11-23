from setuptools import setup, find_packages

setup(
    name='openvoice-tts',
    version='0.1.0',
    description='Instant voice cloning library',
    long_description=open('README.md').read().strip(),
    long_description_content_type='text/markdown',
    keywords=[
        'text-to-speech',
        'tts',
        'voice-clone',
        'zero-shot-tts'
    ],
    url='https://github.com/myshell-ai/OpenVoice',
    author='MyShell',
    author_email='ethan@myshell.ai',
    license='MIT',
    packages=find_packages(include=['openvoice', 'openvoice.*']),
    python_requires='>=3.9,<3.10',
    install_requires=[
        'librosa==0.9.1',
        'faster-whisper==0.9.0',
        'pydub==0.25.1', 
        'wavmark==0.0.3',
        'numpy==1.22.0',
        'eng_to_ipa==0.0.2',
        'inflect==7.0.0',
        'unidecode==1.3.7',
        'whisper-timestamped==1.14.2',
        'pypinyin==0.50.0',
        'cn2an==0.5.22',
        'jieba==0.42.1',
        'gradio==3.48.0',
        'langid==1.1.6',
        'torch>=1.13.0',
        'torchaudio>=0.13.0'
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ]
)
