let count = 0;
const CountVal = document.getElementById('counter_value')
const decBtn = document.getElementById('decrease-btn')
const resBtn = document.getElementById('reset-btn')
const incrBtn = document.getElementById('increase-btn')

function updateDisplay(){
    CountVal.textContent = count;

    CountVal.classList.add('positive','negative','zero')

    if (count > 0){
        Value.classList.add('positive');
    } else if (count < 0){
        Value.classList.add('negative');
    } else Value.classList.add('zero');
}

incrBtn.addEventListener('click', function(){
    count+=1;
    updateDisplay();
});
decBtn.addEventListener('click', function(){
    count-=1;
    updateDisplay();
});
resBtn.addEventListener('click', function(){
    count = 0;
    updateDisplay();
});

updateDisplay();
