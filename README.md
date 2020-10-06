- template borrowed from: https://github.com/weightagnostic/weightagnostic.github.io

- build:

  - git clone https://github.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io.git
  - cd LocalShapeDescriptors.github.io.git

  - if needed, install npm: https://www.npmjs.com/get-npm

  - npm install markdown-it --save
  - npm install markdown-it-katex
  - npm install markdown-it-center-text --save

  - ./bin/make

- run from local server with python -m http.server in base folder, navigate to
  localhost:8000 in browser

-add to this
