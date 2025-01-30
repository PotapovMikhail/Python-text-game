player = {
    'name': '',
    'armor': 0.95,
    'hp': 100,
    'attack': 5,
    'luck': 10,
    'money': 10000,
    'inventory': []
}

enemies = [
    {
        'name': 'Волк', 
        'hp': 10,
        'attack': 10,
        'script': 'Зачем ты здесь? Ты не сможешь меня победить. Принцесса больше не твоя, а чья - не твоя забота. Уходи, пока можешь.',
        'win': 'Ты - достойный противник, но до принцессы тебе всё равно никогда не добраться.',
        'loss': 'Ха! Я же говорил - тебе меня не одолеть. Уходи и не возвращайся.'
    },
    {
        'name': 'Змей Горыныч',
        'hp': 20,
        'attack': 25,
        'script': 'Не ожидал меня встретить? Я, если честно, тоже не думал, что здесь окажусь. После богатырей остаётся только фрилансить, в этот раз сказали защищать долину на пути к замку. В любом случае, ААААААрхрхрархгрх!! Ты не пройдёшь!',
        'win': 'На самом деле, я даже рад, что ты меня победил. Мой босс - дуралей, принцессу не заслужил. Иди дальше. Не зубадь там замолвить за меня словечко. Скажи, что я сражался как лев. Нет.. Как дракон!!',
        'loss': 'Могли бы просто побеседовать. Ты же и сам знал, что у тебя не получится меня убить.. Возвращайся как-нибудь, здесь довольно одиноко.'
    },

    {
        'name': 'Доминик Торетто',
        'hp': 200,
        'attack': 50,
        'script': 'Как ты смог добраться до сюда?! Как ты вообще посмел думать, что можешь со мной сражаться? Ты слаб! Принцесса будет моей, а ты уйдёшь ни с чем. Да будет битва! Самое важное - семья.',
        'win': 'Ты меня убил, но я точно появлюсь в следующей части',
        'loss': 'Прощай..'
    },

    {
        'name': 'Терминатор T-800',
        'hp': 800,
        'attack': 100,
        'script': 'Ты никогда меня не победишь, я Терминатор!',
        'win': "Неет, история повторяется, но помни. I'll be back!",
        'loss': 'Я же говорил меня не победить!'
    }
]


items = {
    '1': {
        'name': 'Яблочный пирог',
        'price': 1500,
        'effect': "(+20%) hp"
    },
    '2': {
        'name': 'Пропуск тренировки',
        'price': 1000
    },
    '3' : {
        'name': 'Очень крутой трофей',
        'price': 10000,
        'effect': "(+5) atk"
    },
    '4':{
        'name':"Пудинг",
        'price': 3000,
        'effect': "(+50) hp"
    },
    '5' : {
        'name':'Яблочный сок',
        'price': 2500,
        'effect':"(+7) luck"
    }
}

