// const word_a = "朝から驚きの連続だ";
// const word_i = "いつもの朝とは様子が違う";
// const word_u = "嬉しい知らせが飛び込んできた";
// const word_e = "駅で急に待ち合わせ。慌てて準備して";
// const word_o = "温泉旅行に出発だ！";

// const outputDiv = document.getElementById("output");
// outputDiv.innerHTML = `
//     <p>あ：${word_a}</p>
//     <p>い：${word_i}</p>
//     <p>う：${word_u}</p>
//     <p>え：${word_e}</p>
//     <p>お：${word_o}</p>
// `;

const wordDict = {
    'あ': ['あなたがいるから', 'あの日の約束を', 'あかるい未来へ'],
    'い': ['いつもそばにいて', '今、始めよう', '命を大切に'],
    'う': ['運命感じて', '嬉しい気持ちを', '宇宙のように広く'],
    'え': ['笑顔の花が咲く', '永遠を願って', '絵のような景色を'],
    'お': ['想いを届けよう', '大きな声で', '思い出を胸に']
};

function generatePoem(chars = ['あ', 'い', 'う', 'え', 'お']) {
    return chars.map(char => {
        const lines = wordDict[char] || [`${char}から始まる言葉がありません`];
        return `${char}：${lines[Math.floor(Math.random() * lines.length)]}`;
    }).join('<br>');
}

window.addEventListener('DOMContentLoaded', () => {
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = generatePoem();
});
