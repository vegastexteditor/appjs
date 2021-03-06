{
  'targets': [
    {
      'target_name': 'pack',
      'dependencies': [
        'appjs'
      ],
      'copies':[
        {
          'destination': '<(module_root_dir)/publish/npm-module',
          'files': [
            '<(module_root_dir)/cli',
            '<(module_root_dir)/lib',
            '<(module_root_dir)/index.js',
            '<(module_root_dir)/examples',
          ],
        }
      ],
      'conditions': [
        ['OS=="mac"', {
          'copies': [
            {
              'destination': '<(module_root_dir)/build/Release',
              'files': [
                '<(module_root_dir)/deps/cef/Release/lib.target/libcef.dylib',
              ]
            }
          ]
        }],
        ['OS=="linux"', {
          'copies': [
            {
              'destination': '<(module_root_dir)/build/Release',
              'files': [
                '<(module_root_dir)/deps/cef/Release/lib.target/libcef.so',
              ]
            }
          ]
        }],
        ['OS=="win"', {
          'copies': [
            {
              'destination': '<(module_root_dir)/build/Release',
              'files': [
                '<(module_root_dir)/deps/cef/Release/libcef.dll',
                '<(module_root_dir)/deps/cef/Release/avcodec-54.dll',
                '<(module_root_dir)/deps/cef/Release/avformat-54.dll',
                '<(module_root_dir)/deps/cef/Release/avutil-51.dll',
                '<(module_root_dir)/deps/cef/Release/d3dcompiler_43.dll',
                '<(module_root_dir)/deps/cef/Release/d3dx9_43.dll',
                '<(module_root_dir)/deps/cef/Release/icudt.dll',
                '<(module_root_dir)/deps/cef/Release/libEGL.dll',
                '<(module_root_dir)/deps/cef/Release/libGLESv2.dll'
              ]
            }
          ]
        }]
      ]
    },
    {
      'target_name': 'appjs',
      'msvs_guid': 'A9D6DC71-C0DC-4549-AEB1-3B15B44E86A9',
      'sources': [ 
        'src/main.cpp',
        'src/appjs.cpp',
        'src/appjs_app.cpp',
        'src/appjs_window.cpp',
        'src/includes/cef_handler.cpp',
        'src/includes/cef.cpp',
        'src/includes/cef_loop.cpp',
        'src/includes/cef_scheme_handler.cpp',
        'src/includes/util.cpp',
      ],
      'dependencies': [
        '<(module_root_dir)/deps/cef/dll_wrapper.gyp:libcef_dll_wrapper'
      ],
      'include_dirs': [
        'src/',
        'deps/cef'
      ],
      'cflags': [
        '-fPIC',
        '-Wall',
        '-std=c++0x'
      ],
      'conditions': [
        ['OS=="mac"', {
          'sources': [
            'src/includes/cef_base_mac.mm',
            'src/includes/cef_handler_mac.mm',
            'src/mac/mainwindow.mm'
          ],
          'defines': [
            '__MAC__',
          ],
          'xcode_settings': {
            'OTHER_LDFLAGS':['-Xlinker -rpath -Xlinker @loader_path/']
          },
          'link_settings': {
            'libraries': [
               '<(module_root_dir)/deps/cef/Release/lib.target/libcef.dylib',
               '<(module_root_dir)/build/Release/cef_dll_wrapper.node'
             ]
          }
        }],
        ['OS=="linux"', {
          'sources': [
            'src/includes/cef_base_gtk.cpp',
            'src/includes/cef_handler_gtk.cpp',
            'src/linux/mainwindow.cpp',
          ],
          'defines': [
            '__LINUX__',
            '<!@(uname -a | grep "Ubuntu" > /dev/null && echo "__UBUNTU__" || echo "__NOTUBUNTU__")'
          ],
          'cflags': [
            '<!@(pkg-config --cflags gtk+-2.0)',
          ],
          'link_settings': {
              'ldflags': [
                '<!@(pkg-config --libs-only-L --libs-only-other gtk+-2.0 gthread-2.0)',
                '-Wl,-R,\'$$ORIGIN/\'',
              ],
              'libraries': [
                '<!@(pkg-config --libs-only-l gtk+-2.0 gthread-2.0)',
                '<(module_root_dir)/deps/cef/Release/lib.target/libcef.so',
                '<(module_root_dir)/build/Release/obj.target/deps/cef/cef_dll_wrapper.node'
              ],
          }
        }],
        ['OS=="win"', {
          'sources': [
            'src/includes/cef_base_win.cpp',
            'src/includes/cef_handler_win.cpp',
            'src/windows/mainwindow.cpp'
          ],
          'defines': [
            '__WIN__',
            '_WINSOCKAPI_'
          ],
          'link_settings': {
              'libraries': [
                'GdiPlus.lib',
                '<(module_root_dir)/deps/cef/lib/Release/libcef.lib',
                '<(module_root_dir)/build/Release/lib/libcef_dll_wrapper.node'
              ],
          },
        }]
      ]
    }
  ]
}
