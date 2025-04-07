const form = document.getElementById('form');
form.onsubmit = async (e) => {
    e.preventDefault();
    const input = document.getElementById('input').value;
    const response = await fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input }),
    });
    const data = await response.json();
    document.getElementById('output').innerText = data.output;
};