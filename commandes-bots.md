# Liste et contenu commandes de bots

Préfixe des commandes : `!`

## Commandes sérieuses

### ask

```markdown
Bonjour, il semblerait que la communauté ne comprenne pas votre question. Êtes-vous sûr d'avoir donné un maximum de détails ? Avec plus de détails (par exemple le code source et l'erreur complète) la communauté sera mieux armée pour comprendre votre problème et vous apporter son aide. Essayez d'être clair et montrez vous patient, une question bien posée attire le regard et trouvera rapidement une réponse 🙂
```

### bienvenue (alias: debutant)

```markdown
**Canaux**
Il y a divers canaux à votre disposition. Certains sont basés sur un thème en général comme `#hardware`, et d'autres sont spécifiques aux langages comme `#python`. Afin de pouvoir accéder aux canaux, vous devez vous attribuer un rôle via <id:customize> et <id:browse>.

**Demander de l'aide**
Pour faire une demande d'aide efficace, veillez à directement poser votre question **en incluant le plus d'informations possibles** au lieu de demander si quelqu'un est disponible.

**Partager son code**
N'utilisez pas de capture d'écran de votre code mais plutôt le Markdown intégré de Discord. Si votre code est trop long, vous pouvez utiliser un service tiers comme https://bin.readthedocs.fr/.
```

```json
{
  "embed":{
    "fields":[{
        "name":"**Canaux**",
        "value":"Il y a divers canaux à votre disposition. Certains sont basés sur un thème en général comme `#hardware`, et d'autres sont spécifiques aux langages comme `#python`. Afin de pouvoir accéder aux canaux, vous devez vous attribuer un rôle via <id:customize> et <id:browse>.",
        "inline":false
      },{
        "name":"Demander de l'aide",
        "value":"Pour faire une demande d'aide efficace, veillez à directement poser votre question **en incluant le plus d'informations possibles** au lieu de demander si quelqu'un est disponible.",
        "inline":false
      },{
        "name":"Partager son code",
        "value":"N'utilisez pas de capture d'écran de votre code mais plutôt le Markdown intégré de Discord. Si votre code est trop long, vous pouvez utiliser un service tiers comme https://bin.readthedocs.fr/.",
        "inline":false
      }],
    "color":8407071
  }
}
```

### borderline

```markdown
NaN ne cautionne pas l'aide apportée sur des sujets où la légalité est douteuse. Vos intentions sont peut-être honnêtes, mais comme il est impossible de vérifier ce qu'il en est réellement, les demandes d'aide sur des sujets légalement problématiques ne seront pas bien vues, voire sanctionnées si répétitives.
```

### code

```json
{
  "embed":{
    "description":"Pour les non-connaisseurs de Discord, il existe un moyen de poster du code bien formaté, lisible et coloré. Référez-vous à la documentation de Discord :\n\n[Documentation Discord](https://support.discord.com/hc/fr/articles/210298617-Bases-de-la-mise-en-forme-de-texte-Markdown-mise-en-forme-du-chat-gras-italique-souligné)\n\nSi votre code est assez long, préférez plutôt l'envoi d'un fichier (avec la bonne extension!) directement, Discord saura le mettre en forme pour qu'on puisse le lire ou le télécharger.\n\nMerci de **ne pas envoyer** de screenshot/photo de votre code directement.",
    "title":"Poster du code (`!code`)",
    "color":8323199
  }
}
```

### cours

```markdown
Voici une liste de cours et documentations pour plusieurs langages (par TnTakara) : <https://learndev.info/>
```

### coursc

```markdown
Pour apprendre le langage C, le mieux en tant que débutant est le cours de Zeste de Savoir (https://zestedesavoir.com/tutoriels/755/le-langage-c-1/). Sinon le livre de Kernighan & Ritchie reste une référence mais pas la plus aisée.
```

### cdebutant

```markdown
Choisir le langage C pour faire un projet est déconseillé de nos jours surtout pour les débutants en programmation. En effet ce langage est remplie de pièges tels que:
- Les undefinied behaviors
- Les fuites de mémoires
- Les use after free
et bien d'autres.
Le C devrait uniquement être choisis si c'est obligatoire par exemple un exercice de cours obligeant l'utilisation de ce langage.
Si vous souhaitez créer un programme ou projet nécessitant de la gestion mémoire et/ou un contrôle fin sur le programme.
Il est recommandé de choisir le langage rust ou le C++.
Plus d'infos sur les idées reçues et pourquoi le C est déconseillé ici: [Les idées reçues sur le C](https://hub.notaname.fr/langages/c/debunk-c.html)
```

### courscpp

```markdown
**Apprendre le C++**
La référence pour l'apprentissage du C++ moderne sont les livres [C++ Primer 5th Edition de S. Lippman](https://www.amazon.fr/C-Primer-Stanley-B-Lippman/dp/0321714113) (à ne pas confondre avec le C++ Primer Plus 6th) et [Le guide du C++ Moderne de débutant à développeur](https://livre.fnac.com/a14868645/Mehdi-Benharrats-Le-guide-du-C-moderne-De-debutant-a-developpeur).

Il existe aussi des bons cours en français et en ligne comme celui de [Zeste de Savoir](https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/).

Une version papier issue du cours de Zeste de Savoir, intitulée "Le guide du C++ moderne - De débutant à développeur", rédigée par Mehdi Benharrats et Benoït Vittupier est disponible ([Site de l'éditeur](https://www.d-booker.fr/cppmoderne/656-le-guide-du-c-moderne-de-debutant-a-developpeur.html)). Ce cours traite d'un ensemble de notions fondamentales et parfois plus approfondies liées à la programmation mais aussi de principes de conception essentiels et d'idiomes particuliers, à propos du langage dans ses versions "modernes".

Attention au cours d'Openclassrooms, celui-ci est obsolète et de mauvaise qualité, nous vous recommandons fortement de vous pencher sur une autre ressource.
```

```json
{
  "embed":{
    "color":1404123,
    "description":"La référence pour l'apprentissage du C++ moderne sont les livres [C++ Primer 5th Edition de S. Lippman](https://www.amazon.fr/C-Primer-Stanley-B-Lippman/dp/0321714113) (à ne pas confondre avec le C++ Primer Plus 6th) et [Le guide du C++ Moderne de débutant à développeur](https://livre.fnac.com/a14868645/Mehdi-Benharrats-Le-guide-du-C-moderne-De-debutant-a-developpeur).\n\nIl existe aussi des bons cours en français et en ligne comme celui de [Zeste de Savoir](https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/).\n\nUne version papier issue du cours de Zeste de Savoir, intitulée \"Le guide du C++ moderne - De débutant à développeur\", rédigée par Mehdi Benharrats et Benoït Vittupier est disponible ([Site de l'éditeur](https://www.d-booker.fr/cppmoderne/656-le-guide-du-c-moderne-de-debutant-a-developpeur.html)). Ce cours traite d'un ensemble de notions fondamentales et parfois plus approfondies liées à la programmation mais aussi de principes de conception essentiels et d'idiomes particuliers, à propos du langage dans ses versions \"modernes\".\n\nAttention au cours d'Openclassrooms, celui-ci est obsolète et de mauvaise qualité, nous vous recommandons fortement de vous pencher sur une autre ressource.",
    "author":{
      "icon_url":"https://cdn.discordapp.com/emojis/324889181740466179.png",
      "name":"Apprendre le C++"
    }
  }
}
```

### courscsharp

```markdown
Voici un ensemble de ressources intéressantes pour commencer votre apprentissage, ou l'approfondir :

- <https://docs.microsoft.com/en-us/dotnet/csharp/> Cours complet sur l'apprentissage du langage
- <https://docs.microsoft.com/fr-fr/aspnet/?view=aspnetcore-2.2#pivot=core> Apprendre ASP.NET (Web).
- <http://www.e-naxos.com/AllDotBlog.html> Ensemble de livres sur : WPF, Xamarin, MVVM, Linq, etc
- <https://codeblog.jonskeet.uk/category/edulinq/> EduLinq, pour comprendre Linq en profondeur
```

### courscss

```markdown
Pour apprendre le HTML et le CSS, je te conseille <https://marksheet.io/> (en anglais), un petit cours pas piqué des hannetons qui surpasse largement celui de OC.
```

### coursjava

```markdown
**Cours sur le langage Java**
:closed_book: **Cours par jmdoudoux**
Cours en français sur le Java, par jmdoudoux : [Développons en Java](https://www.jmdoudoux.fr/java/dej/indexavecframes.htm)
:page_facing_up: **Tutoriels Java2S**
Tutoriels Java, en anglais: [Java2S](http://java2s.com)
:movie_camera: **Cours sur Java par Dominique Liard (Koor.fr)**
Playlists de cours sur Java par Dominique Liard (Koor.fr) :
[Dominique Liard (Koor.fr)](https://www.youtube.com/channel/UCl8T9GRhma8C2PaRfGIjOtA/playlists)
:movie_camera: **Cours sur Java par José Paumard**
Chaine youtube de cours sur Java par José Paumard :
[José Paumard](https://www.youtube.com/channel/UCIatmtIm9z5YEWuHbrUMLsw)
:pushpin: **Messages épinglés**
Pensez à regarder également dans les messages épinglés, des ressources y sont listées.
```

```json
{
  "embed":{
    "color":16292119,
    "fields":[
      {
        "name":":closed_book: Cours par jmdoudoux",
        "value":"Cours en français sur le Java, par jmdoudoux : [Développons en Java](https://www.jmdoudoux.fr/java/dej/indexavecframes.htm)",
        "inline":false
      },
      {
        "name":":page_facing_up: Tutoriels Java2S",
        "value":"Tutoriels Java, en anglais: [Java2S](http://java2s.com)",
        "inline":false
      },
      {
        "name":":movie_camera: Cours sur Java par Dominique Liard (Koor.fr)",
        "value":"Playlists de cours sur Java par Dominique Liard (Koor.fr) : \n[Dominique Liard (Koor.fr)](https://www.youtube.com/channel/UCl8T9GRhma8C2PaRfGIjOtA/playlists)",
        "inline":false
      },
      {
        "name":":movie_camera: Cours sur Java par José Paumard",
        "value":"Chaine youtube de cours sur Java par José Paumard : \n[José Paumard](https://www.youtube.com/channel/UCIatmtIm9z5YEWuHbrUMLsw)",
        "inline":false
      },
      {
        "name":":pushpin: Messages épinglés",
        "value":"Pensez à regarder également dans les messages épinglés, des ressources y sont listées.",
        "inline":false
      }
    ],
    "author":{
      "name":"Cours sur le langage Java",
      "icon_url":"https://cdn.discordapp.com/emojis/324892791966793740.png",
      "url":"https://adoptopenjdk.net"
    }
  }
}
```

### coursjs

```markdown
:movie_camera: **Formation Grafikart (recommandée)**
Cours vidéo en français et gratuit, avec un passage sur Node.js: [Apprendre le JavaScript](https://www.youtube.com/playlist?list=PLjwdMgw5TTLXgsTQE_1PpRkC_yX47ZcGV)
Cours vidéo en français et gratuit: [Apprendre le TypeScript](https://www.youtube.com/playlist?list=PLjwdMgw5TTLX1tQ1qDNHTsy_lrkCt4VW3)
:closed_book: **Cours JavaScript moderne**
Version anglaise: [The Modern JavaScript Tutorial](https://javascript.info) :flag_gb:
Version française: [Le tutoriel JavaScript moderne](https://fr.javascript.info) :flag_fr:
:blue_book: **Eloquent JavaScript**
Cours en anglais sur le JavaScript: [Eloquent JavaScript](https://eloquentjavascript.net)
:blue_book: **You Don't Know JS**
Cours en anglais sur le JavaScript: [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS)
:movie_camera: **FrontendMasters**
Cours vidéos en anglais et payant sur les technologies web Front-End
Les cours ont un __accès gratuit pour 6 mois avec le pack Github Student__
[Frontend Masters](https://frontendmasters.com)
:pushpin: **Messages épinglés**
Pensez à regarder également dans les messages épinglés, des ressources y sont listées.
```

```json
{
  "embed":{
    "color":15981340,
    "fields":[
      {
         "value":"Cours vidéo en français et gratuit, avec un passage sur Node.js: [Apprendre le JavaScript](https://www.youtube.com/playlist?list=PLjwdMgw5TTLXgsTQE_1PpRkC_yX47ZcGV) \nCours vidéo en français et gratuit: [Apprendre le TypeScript](https://www.youtube.com/playlist?list=PLjwdMgw5TTLX1tQ1qDNHTsy_lrkCt4VW3)",
         "inline":false,
         "name":":movie_camera: Formation Grafikart (recommandée)"
      },
      {
         "value":"Version anglaise: [The Modern JavaScript Tutorial](https://javascript.info) :flag_gb:\nVersion française: [Le tutoriel JavaScript moderne](https://fr.javascript.info) :flag_fr:",
         "inline":false,
         "name":":closed_book: Cours JavaScript moderne"
      },
      {
         "value":"Cours en anglais sur le JavaScript: [Eloquent JavaScript](https://eloquentjavascript.net)",
         "inline":false,
         "name":":blue_book: Eloquent JavaScript"
      },
      {
         "value":"Cours en anglais sur le JavaScript: [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS)",
         "inline":false,
         "name":":blue_book: You Don't Know JS"
      },
      {
         "value":"Cours vidéos en anglais et __payant__ sur les technologies web Front-End\nLes cours ont un __accès gratuit pour 6 mois avec le pack Github Student__\n[Frontend Masters](https://frontendmasters.com)",
         "inline":false,
         "name":":movie_camera: FrontendMasters"
      },
      {
         "value":"Pensez à regarder également dans les messages épinglés, des ressources y sont listées.",
         "inline":false,
         "name":":pushpin: Messages épinglés"
      }
    ],
    "author":{
      "name":"Cours sur les langages JavaScript et TypeScript",
      "icon_url":"https://cdn.discordapp.com/emojis/438290351749332993.png",
    }
  }
}
```

### courshtml

```markdown
Pour apprendre le HTML et le CSS, je te conseille <https://marksheet.io/> (en anglais), un petit cours pas piqué des hannetons qui surpasse largement celui de OC.

Alternativement il existe aussi de bons cours en français :
- <https://www.grafikart.fr/formations/html>
- <https://www.grafikart.fr/formations/css>
- <https://developer.mozilla.org/fr/docs/Apprendre/Commencer_avec_le_web/Les_bases_HTML>
```

### courspython

```markdown
Références Python (!courspython)
Cours
🍋 En ligne ZdS
🌐 En ligne SdZ
📖 Cours écrit
🎬 Cours vidéo
Documentation
🐍 Officielle
🔋 Libraries
🔧 Modèle de données
📦 Packaging
Livres
🐿️ Cookbook
📓 Expert Py. Prog.
Articles
:nan: Not a Name
🍊 Zeste de Savoir
🕸️ Fullstack
Conférences
🤵‍♂️ Data Model
👺 Beyond PEP8
🏎️ Concurrency
📌 Regardez aussi les messages épinglés !
En haut à droite de votre écran.
```

```json
{"embed":{"author":{"name":"Références Python (!courspython)","icon_url":"https://cdn.discordapp.com/emojis/436841178936246272.png"},"color":815124,"fields":[{"name":"Cours","value":"🍋 [En ligne ZdS](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/)\n🌐 [En ligne SdZ](https://user.oc-static.com/ftp/livre/python/apprenez_a_programmer_en_python.pdf)\n📖 [Cours écrit](https://inforef.be/swi/download/apprendre_python3_5.pdf)\n🎬 [Cours vidéo](https://www.youtube.com/watch?v=HWxBtxPBCAc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC)","inline":true},{"name":"Documentation","value":"🐍 [Officielle](https://docs.python.org/fr/3/)\n🔋 [Libraries](https://pymotw.com/3/)\n🔧 [Modèle de données](https://docs.python.org/fr/3/reference/datamodel.html)\n📦 [Packaging](https://packaging.python.org/en/latest/)","inline":true},{"name":"Livres","value":"🐿️ [Cookbook](https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/)\n📓 [Expert Py. Prog.](https://www.packtpub.com/product/expert-python-programming-fourth-edition/9781801071109)","inline":true},{"name":"Articles","value":"<:nan:642454964836368386> [Not a Name](https://hub.notaname.fr/langages/python/)\n🍊 [Zeste de Savoir](https://zestedesavoir.com/bibliotheque/?tag=python)\n🕸️ [Fullstack](https://www.fullstackpython.com/)","inline":true},{"name":"Conférences","value":"👺 [Beyond PEP8](https://youtu.be/wf-BqAjZb8M)\n🏎️ [Concurrency](https://youtu.be/9zinZmE3Ogk)\n🤵‍♂️ [Data Model](https://youtu.be/cKPlPJyQrt4)","inline":true},{"name":"📌 Regardez aussi les messages épinglés !","value":"En haut à droite de votre écran.","inline":false}]}}
```

### coursrust

```markdown
:closed_book: Rust Book
La meilleure ressource pour apprendre le Rust est le Book officiel. Une traduction en français est disponible, ainsi qu'une [édition papier et ebook](https://nostarch.com/rust-programming-language-2nd-edition).

:flag_gb: [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) (recommandé)
:flag_fr: [Le langage de programmation Rust](https://jimskapt.github.io/rust-book-fr/)

:blue_book: Idiomatic Rust
Idiomatic Rust liste de nombreuses ressources pour progresser en Rust, découvrir son écosystème, et écrire du code propre et idiomatique : [Idiomatic Rust](https://github.com/mre/idiomatic-rust)

:page_facing_up: Rust by Example
Rust by Example présente les concepts de Rust à travers divers exemples de codes documentés : [Rust by Example](https://doc.rust-lang.org/stable/rust-by-example/)

:pushpin: Messages épinglés
Pensez à regarder également dans les messages épinglés, des ressources y sont listées.
```

```json
{
"embed": {
  "color": 16147968,
  "fields": [
    {
      "name": ":closed_book: Rust Book",
      "value": "La meilleure ressource pour apprendre le Rust est le Book officiel. Une traduction en français est disponible, ainsi qu'une [édition papier et ebook](https://nostarch.com/rust-programming-language-2nd-edition).\n\n:flag_gb: [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) (recommandé)\n:flag_fr: [Le langage de programmation Rust](https://jimskapt.github.io/rust-book-fr/)"
    },
    {
      "name": ":blue_book: Idiomatic Rust",
      "value": "Idiomatic Rust liste de nombreuses ressources pour progresser en Rust, découvrir son écosystème, et écrire du code propre et idiomatique : [Idiomatic Rust](https://github.com/mre/idiomatic-rust)"
    },
    {
      "name": ":page_facing_up: Rust by Example",
      "value": "Rust by Example présente les concepts de Rust à travers divers exemples de codes documentés : [Rust by Example](https://doc.rust-lang.org/stable/rust-by-example/)"
    },
    {
      "name": ":pushpin: Messages épinglés",
      "value": "Pensez à regarder également dans les messages épinglés, des ressources y sont listées."
    }
  ],
  "author": {
    "name": "Cours sur le langage Rust",
    "url": "https://www.rust-lang.org/",
    "icon_url": "https://cdn.discordapp.com/emojis/436842016559857664.png"
  }
}
}
```

### courssql, coursdb
```json
{
  "embed": {
    "color": 15638942,
    "fields": [
      {
        "name": ":flag_gb: SQL Tutorial",
        "value": "(Gratuit) [SQL Tutorial](https://sqlzoo.net/wiki/SQL_Tutorial)"
      },
      {
        "name": ":flag_fr: Sql.sh",
        "value": "(Gratuit) [SQL.sh](https://sql.sh)"
      },
      {
        "name": ":flag_gb: :money_with_wings:  Formation SQL from Zero to Hero (Postgres)",
        "value": "(Payant) [Formation SQL from Zero to Hero (Postgres)](https://www.udemy.com/the-complete-sql-masterclass-for-data-analytics)"
      }
    ],
    "author": {
      "name": "Cours sur les bases de données"
    }
  }
}
```

### crosspost

```markdown
Il existe volontairement plusieurs canaux dédiés à certaines catégories de questions et discussions. Cette distinction par canaux est présente pour éviter de dupliquer les messages. Il est inutile et dérangeant de demander dans un canal de répondre à votre question dans un autre : quelqu'un vous répondra en temps voulu, mais certainement pas ailleurs que celui dans lequel votre question est adaptée.
```

### devbots

```markdown
Informations sur la création de bots Discord

⚠ Avertissement
Pas mal de personnes veulent créer un bot Discord, mais s'il vous plaît, **apprenez déjà un langage de programmation** ainsi que **les outils nécessaires**.
Vous pouvez créer un bot avec différents langages de programmation ( Script, Python, C#, etc.).
Mais cela demande d'avoir des bases dans ce langage et la compréhension de certaines notions.

❓ Je ne comprends rien
Si vous ne comprenez pas ce que vous faites, c'est probablement qu'il vous manque certaines choses et concepts à apprendre.
Veillez aussi à lire et essayer de comprendre les messages d'erreurs.

👍 Les éléments de base
De plus, débuter par la création d'un bot Discord est une mauvaise idée. En effet, la création d'un bot requiert beaucoup de connaissances, parfois, les bases ne suffisent pas.

Voici une liste non-exhaustive des notions dont vous pouvez avoir besoin pour faire un bot :
- les structures de contrôle (if, else, etc.)
- les boucles (for, while, etc.)
- les variables et les structures de données (listes, objets, etc.)
- la gestion des exceptions
- la définition et appel de fonctions
- les classes, les objets, ce que sont les attributs et les méthodes
- l'asynchrone (important) et les événements

🔗 Liens utiles
📚 [Bibliothèques (wrappers) pour le développement de bots Discord](https://discord.com/developers/docs/topics/community-resources#libraries).
📕 [Cours pour apprendre un langage](https://www.learndev.info/fr).
```

### examen / triche / devoirs

```markdown
**Examens:**
Comme indiqué en [règle #2](https://discord.com/channels/323076998576603137/358924179954860033/860920025027575838), la loi française est d'application sur le serveur.

Ainsi, selon la [Loi du 23 décembre 1901 réprimant les fraudes dans les examens et concours publics.](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000314853), toute fraude a un examen est un **délit** passible d’une peine de 3 ans de prison, 9000€ d’amende, d'une interdiction de concourir à un examen pendant 5 ans (ce qui inclus le permis de conduire), et d'une interdiction de s’inscrire à un établissement d’enseignement supérieur pendant 5 ans.

Il est donc **interdit** de demander de l'aide pour un examen.
Nous considérons comme examen tout devoir noté effectué dans l'etablissement scolaire.
*Petit rappel:* Autoriser internet dans un examen ne signifie pas vous autoriser à demander à quelqu'un d'autre de faire le travail à votre place, uniquement que vous êtes autorisé à vous documenter sur Internet.

**Devoirs maisons:**
Nous sommes un peu plus laxistes sur ce point, nous autorisons l'aide concernant les devoirs maisons *mais* ce sera une aide de résolution de problèmes, pas à faire le devoir à votre place. Toute demande afin que quelqu'un fasse le devoir à votre place gratuitement ou contre rétribution est **interdite**.
```

### mentoring

```json
{
  "embed":{
    "description":"Le serveur ne propose pas de système de mentoring, cela necessite que le mentor soit **qualifié** et ce système se base sur le fait qu'une personne seule aurait toute les bonnes réponses.\nCe n'est pas un moyen d'apprentissage recommandée par la communauté NaN.\nNous conseillons plutôt de suivre un des nombreux cours proposés sur le serveur via `!cours`, `!cours{langage}` et les messages épinglés dans les differents canaux.\n\nA noter que le mentoring gratuit ET rémunéré sont interdits ici.\n\nVous êtes bien sûr quand même les bienvenus dans les differents canaux de la communauté pour y poser des questions.",
    "title":"À propos du mentoring (`!mentoring`)",
    "color": 3325119
  }
}
```

### mp, vocal

```markdown
L'aide en message privé (`!mp`, `!vocal`)

Sur Not a Name, on ne préconise ni l'aide en message privé ni l'aide en vocal. Votre problème est peut-être partagé par un autre membre, ou votre question peut en intéresser d'autres. De plus, si une unique personne vous aide et que sa façon de faire est déconseillée, vous vous retrouverez avec d'autres problèmes sur les bras ; là ou une multitude d'autres membres auraient souligné ces mauvaises pratiques.
```

### recrutement

```markdown
La publicité, la présentation des projets et les messages de recrutements sont soumis à une règlementation accrue. (`!recrutement`)

Il existe des salons dédiés à ces messages et l'accès à ces salons est modéré par le staff. Tout message à tendance publicitaire ou de recrutement envoyé en dehors de ces salons ou par messages privés est interdit. Voir la section *Les salons modérés* des <#860920579154772018>
```

### salon

```markdown
Vous ne voyez pas le canal indiqué par les autres utilisateurs ? Voici la marche à suivre : <https://discordapp.com/channels/323076998576603137/699260551758610545/699265804994215997>
```

### scrapping / webscrapping

```json
{
  "embed":{
    "title":"Web-scraping",
    "color":65024,
    "description":"Le scraping de données est la pratique de programmatiquement télécharger des données depuis un site. Il est possible de scraper en forgeant des requêtes HTTP ou bien en automatisant un navigateur web.\n\nLe scraping n'est pas correctement couvert par un cadre légal. Sur NaN, nous n'autorisons le web-scraping que lorsque celui-ci peut s'effectuer dans le respect strict des conditions d'utilisation du site en question. En d'autres termes, lorsqu'un site propose une API et que vous voulez interagir avec ce site : vous *devez* utiliser cette API.\n\nToute demande d'aide concernant le web-scraping doit être accompagné d'une référence vers le passage qui autorise le scraping dans les CGU du site. À défaut, la demande d'aide tombera sous la règle concernant le respect de la loi et sera classée sans suite.\n\nPlus d'informations sur l'état du cadre légal du web-scraping : <https://lexing.be/le-scraping-est-il-legal/>."
  }
}
```

## Commandes "funs"


### johnson

```markdown
<:johnson:324896229987450881><:johnson2:324886127838232576><:johnson:324896229987450881>
<:johnson2:324886127838232576><:johnson:324896229987450881><:johnson2:324886127838232576>
<:johnson:324896229987450881><:johnson2:324886127838232576><:johnson:324896229987450881>
```

### jelareff

```markdown
https://pbs.twimg.com/media/EWj59FlWsAc_AnX.jpg
```

### jokeyou

```markdown
https://tenor.com/view/joke-dumb-gif-8906255
```

### palareff

```markdown
https://pbs.twimg.com/media/ENeXefxUwAAPaiY.jpg
```
### peuk
```
Fais comme nous, pars du principe que Peuk est un sorcier
```
### pinceapain

```markdown
https://tenor.com/WkN5.gif
```
