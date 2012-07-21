versions = {
    'cpython': {
        '2.7.0': {
            'dist': '6fadf5dc9d3e0da6445aa7dbb25e1c4d1403cc48',
            'script': 'python'
        },
        '2.7.1': {
            'dist': '471baf1df04c839af691467c6f41abbcd7d48b31',
            'script': 'python'
        },
        '2.7.2': {
            'dist': '3ae962feefb581b1386dd23400e2299aa7f47ed1',
            'script': 'python'
        },
        '2.7.3': {
            'dist': '4ad1d5064807e42fd4cd8b88dc03c09082a30086',
            'script': 'python'
        },
        '3.2.0': {
            'dist': '939c82fa214efc9ee853e124186e898d1a8ed30d',
            'script': 'python3'
        },
        '3.2.1': {
            'dist': 'ca707a567127ca67ee02c1f4d167303e72924c07',
            'script': 'python3'
        },
        '3.2.2': {
            'dist': '4d8c0089cdfe736494a15ea022dd351dd91f375a',
            'script': 'python3'
        },
        '3.2.3': {
            'dist': 'c6e1779fe45d51f6cd478958702bfff5f603b20e',
            'script': 'python3'
        },
    }
}

versions['cpython']['2.7'] = versions['cpython']['2.7.3']
versions['cpython']['3.2'] = versions['cpython']['3.2.3']

versions['python'] = versions['cpython']