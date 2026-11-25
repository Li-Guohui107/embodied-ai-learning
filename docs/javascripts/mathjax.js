window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true,
    packages: {'[+]': ['ams']}
  },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    ignoreHtmlClass: '.*|',
    processHtmlClass: 'arithmatex'
  },
  chtml: { scale: 1.0 }
};
