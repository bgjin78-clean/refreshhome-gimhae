const generateBtn = document.getElementById('generate');
const container = document.querySelector('.numbers-group');

const getBallColorClass = (num) => {
    if (num <= 10) return 'ball-yellow';
    if (num <= 20) return 'ball-blue';
    if (num <= 30) return 'ball-red';
    if (num <= 40) return 'ball-gray';
    return 'ball-green';
};

const generateSet = () => {
    const numbers = new Set();
    while (numbers.size < 6) {
        numbers.add(Math.floor(Math.random() * 45) + 1);
    }
    return Array.from(numbers).sort((a, b) => a - b);
};

generateBtn.addEventListener('click', () => {
    container.innerHTML = '';
    
    for (let i = 0; i < 5; i++) {
        const row = document.createElement('div');
        row.classList.add('set-row');
        row.style.animationDelay = \`\${i * 0.1}s\`;
        
        const set = generateSet();
        
        set.forEach((num, index) => {
            const ball = document.createElement('div');
            ball.classList.add('number', getBallColorClass(num));
            ball.textContent = num;
            ball.style.animationDelay = \`\${(i * 0.1) + (index * 0.05)}s\`;
            row.appendChild(ball);
        });
        
        container.appendChild(row);
    }
});
