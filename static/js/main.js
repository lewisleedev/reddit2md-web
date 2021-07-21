function copyToClipboard(divId) {
    var range = document.createRange();
    var btn = document.getElementById("copy-btn");
    range.selectNode(document.getElementById(divId));
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand("copy");
    window.getSelection().removeAllRanges();
    btn.innerHTML = 'Copied!';
}

function downloadInnerHtml(filename, elId, mimeType) {
    var elHtml = document.getElementById(elId).innerText;
    var link = document.createElement('a');
    mimeType = mimeType || 'text/plain';
    link.setAttribute('download', filename);
    link.setAttribute('href', 'data:' + mimeType  +  ';charset=utf-8,' + encodeURIComponent(elHtml));
    link.click();
}

const form = document.getElementById("main-form")

form.onsubmit = function() {
    let submitBtn = document.getElementById("submit-btn")
    submitBtn.value = 'Loading...'
}