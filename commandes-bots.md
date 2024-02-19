# Liste et contenu commandes de bots

Préfixe des commandes : `!`

## Commandes sérieuses

### ask

```markdown
>>> Bonjour, il semblerait que la communauté ne comprenne pas votre question. Êtes-vous sûr d'avoir donné un maximum de détails ? Avec plus de détails (par exemple le code source et l'erreur complète) la communauté sera mieux armée pour comprendre votre problème et vous apporter son aide. Essayez d'être clair et montrez vous patient, une question bien posée attire le regard et trouvera rapidement une réponse 🙂
```

### bienvenue (alias: debutant)

```markdown
>>> **Canaux**
Il y a divers canaux à votre disposition. Certains sont basés sur un thème en général comme [#hardware](<https://discord.com/channels/323076998576603137/405326910118166548>), et d'autres sont spécifiques aux langages comme [#python](<https://discord.com/channels/323076998576603137/358724995159031820>). Vous pouvez choisir les canaux à afficher dans les sections <id:customize> et <id:browse>.

**Demander de l'aide**
Pour demander de l'aide efficacement, veillez à directement poser votre question **en incluant le plus d'informations possible** au lieu de demander si quelqu'un est disponible.

**Partager son code**
N'envoyez pas de capture d'écran de votre code, utilisez plutôt le Markdown intégré de Discord. Si votre code est trop long, vous pouvez utiliser un service tiers comme <https://bin.readthedocs.fr/>.
```

```json
{"embed":{"fields":[{"name":"**Canaux**","value":"Il y a divers canaux à votre disposition. Certains sont basés sur un thème en général comme [#hardware](<https://discord.com/channels/323076998576603137/405326910118166548>), et d'autres sont spécifiques aux langages comme [#python](<https://discord.com/channels/323076998576603137/358724995159031820>). Vous pouvez choisir les canaux à afficher dans les sections <id:customize> et <id:browse>.","inline":false},{"name":"Demander de l'aide","value":"Pour faire une demande d'aide efficace, veillez à directement poser votre question **en incluant le plus d'informations possibles** au lieu de demander si quelqu'un est disponible.","inline":false},{"name":"Partager son code","value":"N'envoyez pas de capture d'écran de votre code, utilisez plutôt le Markdown intégré de Discord. Si votre code est trop long, vous pouvez utiliser un service tiers comme <https://bin.readthedocs.fr/>.","inline":false}],"color":8407071}}
```

### borderline

```markdown
>>> NaN ne cautionne pas l'aide apportée sur des sujets où la légalité est douteuse. Vos intentions sont peut-être honnêtes, mais comme il est impossible de vérifier ce qu'il en est réellement, les demandes d'aide sur des sujets légalement problématiques ne seront pas bien vues, voire sanctionnées si répétitives.
```

### code

```markdown
>>> ### Poster du code (`!code`)

Pour les non-connaisseurs de Discord, il existe un moyen de poster du code bien formaté, lisible et coloré. Référez-vous à la documentation de Discord :

[Documentation Discord](<https://support.discord.com/hc/fr/articles/210298617-Bases-de-la-mise-en-forme-de-texte-Markdown-mise-en-forme-du-chat-gras-italique-souligné>)

Si votre code est assez long, préférez plutôt l'envoi d'un fichier (avec la bonne extension !) directement, Discord saura le mettre en forme pour qu'on puisse le lire ou le télécharger.

Merci de **ne pas envoyer** de screenshot/photo de votre code directement.
```

```json
{"embed":{"description":"Pour les non-connaisseurs de Discord, il existe un moyen de poster du code bien formaté, lisible et coloré. Référez-vous à la documentation de Discord :\n\n[Documentation Discord](https://support.discord.com/hc/fr/articles/210298617-Bases-de-la-mise-en-forme-de-texte-Markdown-mise-en-forme-du-chat-gras-italique-souligné)\n\nSi votre code est assez long, préférez plutôt l'envoi d'un fichier (avec la bonne extension!) directement, Discord saura le mettre en forme pour qu'on puisse le lire ou le télécharger.\n\nMerci de **ne pas envoyer** de screenshot/photo de votre code directement.","title":"Poster du code (`!code`)","color":8323199}}
```

### cours

```markdown
>>> Voici une liste de cours et documentations pour plusieurs langages (par TnTakara) : <https://learndev.info/>
```

### coursc

```markdown
>>> Pour apprendre le langage C, le mieux en tant que débutant est le cours de [Zeste de Savoir](<https://zestedesavoir.com/tutoriels/755/le-langage-c-1/>). Sinon le livre de Kernighan & Ritchie reste une référence mais pas la plus aisée.
```

### courscpp

```markdown
>>> ### Apprendre le C++

La référence pour l'apprentissage du C++ moderne sont les livres [C++ Primer 5th Edition de S. Lippman](<https://www.amazon.fr/C-Primer-Stanley-B-Lippman/dp/0321714113>) (à ne pas confondre avec le C++ Primer Plus 6th) et [Le guide du C++ Moderne de débutant à développeur](<https://livre.fnac.com/a14868645/Mehdi-Benharrats-Le-guide-du-C-moderne-De-debutant-a-developpeur>).

Il existe aussi des bons cours en français et en ligne comme celui de [Zeste de Savoir](<https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/>).

Une version papier issue du cours de Zeste de Savoir, intitulée "Le guide du C++ moderne - De débutant à développeur", rédigée par Mehdi Benharrats et Benoït Vittupier est disponible ([Site de l'éditeur](<https://www.d-booker.fr/cppmoderne/656-le-guide-du-c-moderne-de-debutant-a-developpeur.html>)). Ce cours traite d'un ensemble de notions fondamentales et parfois plus approfondies liées à la programmation mais aussi de principes de conception essentiels et d'idiomes particuliers, à propos du langage dans ses versions "modernes".

Attention au cours d'Openclassrooms, celui-ci est obsolète et de mauvaise qualité, nous vous recommandons fortement de vous pencher sur une autre ressource.
```

```json
{"embed":{"color":1404123,"description":"La référence pour l'apprentissage du C++ moderne sont les livres [C++ Primer 5th Edition de S. Lippman](https://www.amazon.fr/C-Primer-Stanley-B-Lippman/dp/0321714113) (à ne pas confondre avec le C++ Primer Plus 6th) et [Le guide du C++ Moderne de débutant à développeur](https://livre.fnac.com/a14868645/Mehdi-Benharrats-Le-guide-du-C-moderne-De-debutant-a-developpeur).\n\nIl existe aussi des bons cours en français et en ligne comme celui de [Zeste de Savoir](https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/).\n\nUne version papier issue du cours de Zeste de Savoir, intitulée \"Le guide du C++ moderne - De débutant à développeur\", rédigée par Mehdi Benharrats et Benoït Vittupier est disponible ([Site de l'éditeur](https://www.d-booker.fr/cppmoderne/656-le-guide-du-c-moderne-de-debutant-a-developpeur.html)). Ce cours traite d'un ensemble de notions fondamentales et parfois plus approfondies liées à la programmation mais aussi de principes de conception essentiels et d'idiomes particuliers, à propos du langage dans ses versions \"modernes\".\n\nAttention au cours d'Openclassrooms, celui-ci est obsolète et de mauvaise qualité, nous vous recommandons fortement de vous pencher sur une autre ressource.","author":{"icon_url":"https://cdn.discordapp.com/emojis/324889181740466179.png","name":"Apprendre le C++"}}}
```

### courscsharp

```markdown
>>> ### :langage_csharp: Cours sur le langage C#

**:closed_book: Cours C# par Microsoft**
Cours en français sur le C#: [C# Documentation](<https://docs.microsoft.com/en-us/dotnet/csharp/>)

**:blue_book: Apprendre ASP.Net (Web)**
Cours et documentation sur le framework ASP.Net: [Documentation d'ASP.Net](<https://docs.microsoft.com/fr-fr/aspnet/core/>)

**:blue_book: EduLinq, comprendre Linq en profondeur**
Cours en anglais sur Linq: [Edulinq](<https://codeblog.jonskeet.uk/category/edulinq/>)

**:book: Ensemble de livres**
Ensemble de livres sur WPF, Xamarin, MVVM, Linq, ... : [Collection All Dot Blog](<https://www.e-naxos.com/AllDotBlog.html>)

**:pushpin: Messages épinglés**
Pensez à regarder également dans les messages épinglés, des ressources y sont listées.
```

### coursflex

```markdown
>>> ### :langage_css: Apprentissage des Flexbox 📕
Lex flexbox sont une méthode de mise en page moderne qui permet de positionner des éléments sur une page.

- Exercice interactif pour apprendre et s’entraîner: [Flexbox Froggy](<https://flexboxfroggy.com/#fr>)
- Cours illustré très qualitatif en anglais: [Guide to Flexbox, CSSTricks](<https://css-tricks.com/snippets/css/a-guide-to-flexbox/>)
- Documentation: [Flexbox - MDN](<https://developer.mozilla.org/fr/docs/Learn/CSS/CSS_layout/Flexbox>)

**Apprentissage de Grid 📘**
Grid est un système de layout basé sur les grilles qui permet de concevoir des interfaces basées sur des grilles.

- Exercice interactif pour apprendre et s’entraîner: [Grid Garden](<https://cssgridgarden.com/#fr>)
- Cours illustré très qualitatif en anglais: [Guide to Grid, CSSTricks](<https://css-tricks.com/snippets/css/complete-guide-grid/>)
- Documentation: [Grid - MDN](<https://developer.mozilla.org/fr/docs/Learn/CSS/CSS_layout/Grids>)

**Cours vidéo 🎥**
- Cours très qualitatif en anglais donné par Jen Kramer: [Grids and Flexbox - Frontendmasters](<https://frontendmasters.com/courses/css-grids-flexbox/>)
- Cours très qualitatif donné par Grafikart: [Formation CSS - Grafikart](<https://grafikart.fr/formations/css>)
```

```json
{"embed":{"fields":[{"value":"Lex flexbox sont une méthode de mise en page moderne qui permet de positionner des éléments sur une page.\n\n- Exercice interactif pour apprendre et s’entraîner: [Flexbox Froggy](https://flexboxfroggy.com/#fr)\n- Cours illustré très qualitatif en anglais: [Guide to Flexbox, CSSTricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) \n- Documentation: [Flexbox - MDN](https://developer.mozilla.org/fr/docs/Learn/CSS/CSS_layout/Flexbox)","inline":false,"name":"Apprentissage des Flexbox :closed_book:"},{"value":"Grid est un système de layout  basé sur les grilles qui permet de concevoir des interfaces basées sur des grilles.\n\n- Exercice interactif pour apprendre et s’entraîner: [Grid Garden](https://cssgridgarden.com/#fr)\n- Cours illustré très qualitatif en anglais: [Guide to Grid, CSSTricks](https://css-tricks.com/snippets/css/complete-guide-grid/) \n- Documentation: [Grid - MDN](https://developer.mozilla.org/fr/docs/Learn/CSS/CSS_layout/Grids)","inline":false,"name":"Apprentissage de Grid :blue_book:"},{"value":"- Cours très qualitatif en anglais donné par Jen Kramer: [Grids and Flexbox - Frontendmasters](https://frontendmasters.com/courses/css-grids-flexbox/) \n- Cours très qualitatif donné par Grafikart: [Formation CSS - Grafikart](https://grafikart.fr/formations/css)","inline":false,"name":"Cours vidéo :movie_camera:"}],"color":10965038}}
```

### courshtml / courscss

```markdown
>>> ### <:langage_html:436841854328242181> Cours sur les langages HTML et CSS
**📕 Marksheet**
Cours en anglais sur le HTML et CSS surpassant celui de OC: [Marksheet](<https://marksheet.io>)

**🎥 Formations vidéo par Grafikart**
- Formation HTML: [Apprendre l'HTML](<https://www.grafikart.fr/formations/html>)
- Formation CSS: [Découverte du CSS](<https://www.grafikart.fr/formations/css>)

**📘 Cours du MDN**
Cours publié par le MDN sur le HTML: [Les bases du HTML](<https://developer.mozilla.org/fr/docs/Apprendre/Commencer_avec_le_web/Les_bases_HTML>)

**📌 Messages épinglés**
Pensez à regarder également dans les messages épinglés, des ressources y sont listées.
```

### coursjava

```markdown
>>> ### :langage_java: Cours sur le langage Java

**📕 Cours par jmdoudoux**
Cours en français sur le Java, par jmdoudoux : [Développons en Java](<https://www.jmdoudoux.fr/java/dej/indexavecframes.htm>)

**📄 Tutoriels Java2S**
Tutoriels Java, en anglais : [Java2S](<http://java2s.com>)

**🎥 Cours sur Java par Dominique Liard (Koor.fr)**
Playlists de cours sur Java par Dominique Liard (Koor.fr) : [Dominique Liard (Koor.fr)](<https://www.youtube.com/channel/UCl8T9GRhma8C2PaRfGIjOtA/playlists>)

**🎥 Cours sur Java par José Paumard**
Chaine youtube de cours sur Java par José Paumard : [José Paumard](<https://www.youtube.com/channel/UCIatmtIm9z5YEWuHbrUMLsw>)

**:pushpin: Messages épinglés**
Pensez à regarder également dans les messages épinglés, des ressources y sont listées.
```

```json
{"embed":{"color":16292119,"fields":[{"name":":closed_book: Cours par jmdoudoux","value":"Cours en français sur le Java, par jmdoudoux : [Développons en Java](https://www.jmdoudoux.fr/java/dej/indexavecframes.htm)","inline":false},{"name":":page_facing_up: Tutoriels Java2S","value":"Tutoriels Java, en anglais : [Java2S](http://java2s.com)","inline":false},{"name":":movie_camera: Cours sur Java par Dominique Liard (Koor.fr)","value":"Playlists de cours sur Java par Dominique Liard (Koor.fr) : \n[Dominique Liard (Koor.fr)](https://www.youtube.com/channel/UCl8T9GRhma8C2PaRfGIjOtA/playlists)","inline":false},{"name":":movie_camera: Cours sur Java par José Paumard","value":"Chaine youtube de cours sur Java par José Paumard : \n[José Paumard](https://www.youtube.com/channel/UCIatmtIm9z5YEWuHbrUMLsw)","inline":false},{"name":":pushpin: Messages épinglés","value":"Pensez à regarder également dans les messages épinglés, des ressources y sont listées.","inline":false}],"author":{"name":"Cours sur le langage Java","icon_url":"https://cdn.discordapp.com/emojis/324892791966793740.png","url":"https://adoptopenjdk.net"}}}
```

### coursjs

```markdown
>>> ### :langage_js: :langage_ts: Cours sur les langages JavaScript et TypeScript

**🎥 Formation Grafikart (recommandée)**
Cours vidéo en français et gratuit, avec un passage sur Node.js: [Apprendre le JavaScript](<https://www.youtube.com/playlist?list=PLjwdMgw5TTLXgsTQE_1PpRkC_yX47ZcGV>)
Cours vidéo en français et gratuit: [Apprendre le TypeScript](<https://www.youtube.com/playlist?list=PLjwdMgw5TTLX1tQ1qDNHTsy_lrkCt4VW3>)

**📕 Cours JavaScript moderne**
Version anglaise: [The Modern JavaScript Tutorial](<https://javascript.info>) :flag_gb:
Version française: [Le tutoriel JavaScript moderne](<https://fr.javascript.info>) :flag_fr:

**📘 Eloquent JavaScript**
Cours en anglais sur le JavaScript: [Eloquent JavaScript](<https://eloquentjavascript.net>)

**📘 You Don't Know JS**
Cours en anglais sur le JavaScript: [You Don't Know JS](<https://github.com/getify/You-Dont-Know-JS>)

**🎥 FrontendMasters**
Cours vidéos en anglais et payant sur les technologies web Front-End: [Frontend Masters](<https://frontendmasters.com>)
Les cours ont un __accès gratuit pour 6 mois avec le pack Github Student__.

**:pushpin: Messages épinglés**
Pensez à regarder également dans les messages épinglés, des ressources y sont listées.
```

```json
{"embed":{"color":15981340,"fields":[{"value":"Cours vidéo en français et gratuit, avec un passage sur Node.js: [Apprendre le JavaScript](https://www.youtube.com/playlist?list=PLjwdMgw5TTLXgsTQE_1PpRkC_yX47ZcGV) \nCours vidéo en français et gratuit: [Apprendre le TypeScript](https://www.youtube.com/playlist?list=PLjwdMgw5TTLX1tQ1qDNHTsy_lrkCt4VW3)","inline":false,"name":":movie_camera: Formation Grafikart (recommandée)"},{"value":"Version anglaise: [The Modern JavaScript Tutorial](https://javascript.info) :flag_gb:\nVersion française: [Le tutoriel JavaScript moderne](https://fr.javascript.info) :flag_fr:","inline":false,"name":":closed_book: Cours JavaScript moderne"},{"value":"Cours en anglais sur le JavaScript: [Eloquent JavaScript](https://eloquentjavascript.net)","inline":false,"name":":blue_book: Eloquent JavaScript"},{"value":"Cours en anglais sur le JavaScript: [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS)","inline":false,"name":":blue_book: You Don't Know JS"},{"value":"Cours vidéos en anglais et __payant__ sur les technologies web Front-End: [Frontend Masters](https://frontendmasters.com)\nLes cours ont un __accès gratuit pour 6 mois avec le pack Github Student__.","inline":false,"name":":movie_camera: FrontendMasters"},{"value":"Pensez à regarder également dans les messages épinglés, des ressources y sont listées.","inline":false,"name":":pushpin: Messages épinglés"}],"author":{"name":"Cours sur les langages JavaScript et TypeScript","icon_url":"https://cdn.discordapp.com/emojis/438290351749332993.png",}}}
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
🦎 Fluent
🐿️ Cookbook
🪷 Expert Py. Prog.
📚 More books
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

```markdown
> ### <:langage_python:436841178936246272> Références Python (`!courspython`)
> 
> **Cours**                            **Documentation**
> 🍋 [En ligne ZdS](<https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/>)        🐍 [Officielle](<https://docs.python.org/fr/3/>)
> 🌐 [En ligne SdZ](<https://user.oc-static.com/ftp/livre/python/apprenez_a_programmer_en_python.pdf>)        🔋 [Libraries](<https://pymotw.com/3/>)
> 📖 [Cours écrit](<https://inforef.be/swi/download/apprendre_python3_5.pdf>)          🔧 [Data Model](<https://docs.python.org/fr/3/reference/datamodel.html>)
> 🎬 [Cours vidéo](<https://www.youtube.com/watch?v=HWxBtxPBCAc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC>)         📦 [Packaging](<https://packaging.python.org/en/latest/>)
> 
> **Articles**                        **Conférences**
> <:nan:642454964836368386> [Not a Name](<https://hub.notaname.fr/langages/python/>)          👺 [Beyond PEP8](<https://youtu.be/wf-BqAjZb8M>)
> 🍊 [Zeste de Savoir](<https://zestedesavoir.com/bibliotheque/?tag=python>)   🏎️ [Concurrency](<https://youtu.be/9zinZmE3Ogk>)
> 🕸️ [Fullstack](<https://www.fullstackpython.com/>)              🤵‍♂️ [Data Model](<https://youtu.be/cKPlPJyQrt4>)
> 
> **Livres**
> 🦎 [Fluent](<https://fluentpython.com/>)
> 🐿️ [Cookbook](<https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/>)
> 🪷 [Expert](<https://www.packtpub.com/product/expert-python-programming-fourth-edition/9781801071109>)
> 📚 [More books](<https://realpython.com/best-python-books/>)
> 
> **📌 Regardez aussi les messages épinglés !**
> En haut à droite de votre écran.
```

### coursrust

```markdown
>>> ### :langage_rust: Cours sur le langage Rust

**📕 Rust Book**
La meilleure ressource pour apprendre le Rust est le [Book officiel](<https://doc.rust-lang.org/book/>). Une traduction en français est disponible, ainsi qu'une édition [papier et ebook](<https://nostarch.com/rust-programming-language-2nd-edition>).

- :flag_gb: [The Rust Programming Language](<https://doc.rust-lang.org/stable/book/>) (recommandé)
- :flag_fr: [Le langage de programmation Rust](<https://jimskapt.github.io/rust-book-fr/>)

**📘 Idiomatic Rust**
Idiomatic Rust liste de nombreuses ressources pour progresser en Rust, découvrir son écosystème, et écrire du code propre et idiomatique : [Idiomatic Rust](<https://github.com/mre/idiomatic-rust>)

**📄 Rust by Example**
Rust by Example présente les concepts de Rust à travers divers exemples de codes documentés : [Rust by Example](<https://doc.rust-lang.org/stable/rust-by-example/>)

**:pushpin: Messages épinglés**
Pensez à regarder également dans les messages épinglés, des ressources y sont listées.
```

```json
{"embed":{"author":{"url":"https://www.rust-lang.org/","icon_url":"https://cdn.discordapp.com/emojis/436842016559857664.png","name":"Cours sur le langage Rust"},"color":16147968,"content_scan_version":1,"fields":[{"inline":false,"name":":closed_book: Rust Book","value":"La meilleure ressource pour apprendre le Rust est le [Book officiel](<https://doc.rust-lang.org/book/>). Une traduction en français est disponible, ainsi qu'une [édition papier et ebook](https://nostarch.com/rust-programming-language-2nd-edition).\n\n:flag_gb: [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) (recommandé)\n:flag_fr: [Le langage de programmation Rust](https://jimskapt.github.io/rust-book-fr/)"},{"inline":false,"name":":blue_book: Idiomatic Rust","value":"Idiomatic Rust liste de nombreuses ressources pour progresser en Rust, découvrir son écosystème, et écrire du code propre et idiomatique : [Idiomatic Rust](https://github.com/mre/idiomatic-rust)"},{"inline":false,"name":":page_facing_up: Rust by Example","value":"Rust by Example présente les concepts de Rust à travers divers exemples de codes documentés : [Rust by Example](https://doc.rust-lang.org/stable/rust-by-example/)"},{"inline":false,"name":":pushpin: Messages épinglés","value":"Pensez à regarder également dans les messages épinglés, des ressources y sont listées."}]}}
```

### courssql, coursdb

```markdown
>>> ### Cours sur les bases de données

**:flag_gb: 💸  Formation SQL from Zero to Hero (Postgres)**
(Gratuit) [SQL Tutorial](<https://sqlzoo.net/wiki/SQL_Tutorial>)

**:flag_fr: Sql.sh**
(Gratuit) [SQL.sh](<https://sql.sh>)

**:flag_gb: 💸  Formation SQL from Zero to Hero (Postgres)**
(Payant) [Formation SQL from Zero to Hero (Postgres)](<https://www.udemy.com/the-complete-sql-masterclass-for-data-analytics>)
```

```json
{"embed":{"color":15638942,"fields":[{"name":":flag_gb: SQL Tutorial","value":"(Gratuit) [SQL Tutorial](https://sqlzoo.net/wiki/SQL_Tutorial)"},{"name":":flag_fr: Sql.sh","value":"(Gratuit) [SQL.sh](https://sql.sh)"},{"name":":flag_gb: :money_with_wings:  Formation SQL from Zero to Hero (Postgres)","value":"(Payant) [Formation SQL from Zero to Hero (Postgres)](https://www.udemy.com/the-complete-sql-masterclass-for-data-analytics)"}],"author":{"name":"Cours sur les bases de données"}}}
```

### crosspost

```markdown
>>> Il existe volontairement plusieurs canaux dédiés à certaines catégories de questions et discussions. Cette distinction par canaux est présente pour éviter de dupliquer les messages. Il est inutile et dérangeant de demander dans un canal de répondre à votre question dans un autre : quelqu'un vous répondra en temps voulu, mais certainement pas ailleurs que celui dans lequel votre question est adaptée.
```

### devbots

```markdown
# Informations sur la création de bots Discord

## ⚠ Avertissement
Pas mal de personnes veulent créer un bot Discord, mais s'il vous plaît, **apprenez déjà un langage de programmation** ainsi que **les outils nécessaires**.
Vous pouvez créer un bot avec différents langages de programmation ( Script, Python, C#, etc.).
Mais cela demande d'avoir des bases dans ce langage et la compréhension de certaines notions.

## ❓ Je ne comprends rien
Si vous ne comprenez pas ce que vous faites, c'est probablement qu'il vous manque certaines choses et concepts à apprendre.
Veillez aussi à lire et essayer de comprendre les messages d'erreurs.

## 👍 Les éléments de base
De plus, débuter par la création d'un bot Discord est une mauvaise idée. En effet, la création d'un bot requiert beaucoup de connaissances, parfois, les bases ne suffisent pas.

Voici une liste non-exhaustive des notions dont vous pouvez avoir besoin pour faire un bot :
- les structures de contrôle (if, else, etc.)
- les boucles (for, while, etc.)
- les variables et les structures de données (listes, objets, etc.)
- la gestion des exceptions
- la définition et appel de fonctions
- les classes, les objets, ce que sont les attributs et les méthodes
- l'asynchrone (important) et les événements

## 🔗 Liens utiles
📚 [Bibliothèques (wrappers) pour le développement de bots Discord](https://discord.com/developers/docs/topics/community-resources#libraries).
📕 [Cours pour apprendre un langage](https://www.learndev.info/fr).
```

```json
{"embed":{"fields":[{"name":":warning: Avertissement","inline":false,"value":"Pas mal de personnes veulent créer un bot Discord, mais s'il vous plaît, **apprenez déjà un langage de programmation** ainsi que **les outils nécessaires**.\nVous pouvez créer un bot avec différents langages de programmation (JavaScript, Python, C#, etc.). \nMais cela demande d'avoir des bases dans ce langage et la compréhension de certaines notions."},{"name":":question: Je ne comprends rien","inline":false,"value":"Si vous ne comprenez pas ce que vous faites, c'est probablement qu'il vous manque certaines choses et concepts à apprendre. \nVeillez aussi à lire et essayer de comprendre les messages d'erreurs."},{"name":":thumbup: Les éléments de base","inline":false,"value":"De plus, débuter par la création d'un bot Discord est une mauvaise idée. En effet, la création d'un bot requiert beaucoup de connaissances, parfois, les bases ne suffisent pas.\n\nVoici une liste non-exhaustive des notions dont vous pouvez avoir besoin pour faire un bot :\n- les structures de contrôle (if, else, etc.)\n- les boucles (for, while, etc.)\n- les variables et les structures de données (listes, objets, etc.)\n- la gestion des exceptions\n- la définition et appel de fonctions\n- les classes, les objets, ce que sont les attributs et les méthodes\n- l'asynchrone (important) et les événements"},{"name":":link: Liens utiles","inline":false,"value":":books: [Bibliothèques (wrappers) pour le développement de bots Discord](https://discord.com/developers/docs/topics/community-resources#libraries).\n:closed_book: [Cours pour apprendre un langage](https://www.learndev.info/fr)."}],"title":"Informations sur la création de bots Discord","color":10655420,"url":"https://discord.com/developers/docs/intro"}}
```

### examen / triche / devoirs

```markdown
>>> ### Examens, triche et devoirs (`!examen`, `!triche`, `!devoirs`)

**Examens:**
Comme indiqué en [règle #2](<https://discord.com/channels/323076998576603137/358924179954860033/860920025027575838>), la loi française est d'application sur le serveur.

Ainsi, selon la [Loi du 23 décembre 1901 réprimant les fraudes dans les examens et concours publics](<https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000314853>), toute fraude a un examen est un **délit** passible d’une peine de 3 ans de prison, 9000€ d’amende, d'une interdiction de concourir à un examen pendant 5 ans (ce qui inclus le permis de conduire), et d'une interdiction de s’inscrire à un établissement d’enseignement supérieur pendant 5 ans.

Il est donc **interdit** de demander de l'aide pour un examen.
Nous considérons comme examen tout devoir noté effectué dans l'établissement scolaire.
*Petit rappel:* Autoriser internet dans un examen ne signifie pas vous autoriser à demander à quelqu'un d'autre de faire le travail à votre place, uniquement que vous êtes autorisé à vous documenter sur Internet.

**Devoirs maisons:**
Nous sommes un peu plus laxistes sur ce point, nous autorisons l'aide concernant les devoirs maisons *mais* ce sera une aide de résolution de problèmes, pas à faire le devoir à votre place. Toute demande afin que quelqu'un fasse le devoir à votre place gratuitement ou contre rétribution est **interdite**.
```

```json
{"embed":{"description":"**Examens:**\nComme indiqué en [règle #2](<https://discord.com/channels/323076998576603137/358924179954860033/860920025027575838>), la loi française est d'application sur le serveur.\n\nAinsi, selon la [Loi du 23 décembre 1901 réprimant les fraudes dans les examens et concours publics](<https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000314853>), toute fraude a un examen est un **délit** passible d’une peine de 3 ans de prison, 9000€ d’amende, d'une interdiction de concourir à un examen pendant 5 ans (ce qui inclus le permis de conduire), et d'une interdiction de s’inscrire à un établissement d’enseignement supérieur pendant 5 ans.\n\nIl est donc **interdit** de demander de l'aide pour un examen.\nNous considérons comme examen tout devoir noté effectué dans l'établissement scolaire.\n*Petit rappel:* Autoriser internet dans un examen ne signifie pas vous autoriser à demander à quelqu'un d'autre de faire le travail à votre place, uniquement que vous êtes autorisé à vous documenter sur Internet.\n\n**Devoirs maisons:**\nNous sommes un peu plus laxistes sur ce point, nous autorisons l'aide concernant les devoirs maisons *mais* ce sera une aide de résolution de problèmes, pas à faire le devoir à votre place. Toute demande afin que quelqu'un fasse le devoir à votre place gratuitement ou contre rétribution est **interdite**.","title":"Examens, triche et devoirs (`!examen`, `!triche`, `!devoirs`)"}}
```

### gpt
```markdown
>>> ### 🤖 Les réponses générées par IA (`!gpt`, `chatgpt`)

L'intelligence artificielle étant devenue largement accessible au public, un grand nombre de personnes sont tentées de poser leurs questions techniques à ces programmes en pensant obtenir une réponse fiable. Ce n'est pas une bonne idée, les réponses données par ces programmes sont loin d'être fiables et peuvent induire en erreur les débutants. Un certain nombre d'erreurs difficiles à déceler aux premiers abords peuvent se glisser dans une réponse globalement bien rédigée, donnant l'illusion d'une réponse valable et de bonne qualité, mais qui dans la pratique peut avoir des effets négatifs sur les projets qui se baseront dessus.
De plus, nous vous rappelons que NaN est une serveur __communautaire__, les gens qui posent des questions et demandent de l'aide doivent pouvoir discuter avec des humains qui seront en capacité de comprendre leurs besoins, le serveur n'a pas vocation à se transformer en une sorte de chatbot géant ou ne seraient échangées plus que des réponses générées automatiquement...

Pour ces raisons, il est **interdit** d'utiliser ChatGPT ou toute autre IA générative pour répondre aux questions des membres.

Pour plus d'informations à ce sujet, voir par exemple la [Politique de Stack Overflow](<https://stackoverflow.com/help/ai-policy>)
```

### mentoring

```markdown
>>> ### À propos du mentoring

Le serveur ne propose pas de système de mentoring, cela necessite que le mentor soit **qualifié** et ce système se base sur le fait qu'une personne seule aurait toute les bonnes réponses.
Ce n'est pas un moyen d'apprentissage recommandé par la communauté NaN.
Nous conseillons plutôt de suivre un des nombreux cours proposés sur le serveur via `!cours`, `!cours{langage}` et les messages épinglés dans les differents canaux.

À noter que le mentoring gratuit ET rémunéré sont interdits ici.

Vous êtes bien sûr quand même les bienvenus dans les differents canaux de la communauté pour y poser des questions.
```

```json
{"embed":{"description":"Le serveur ne propose pas de système de mentoring, cela necessite que le mentor soit **qualifié** et ce système se base sur le fait qu'une personne seule aurait toute les bonnes réponses.\nCe n'est pas un moyen d'apprentissage recommandé par la communauté NaN.\nNous conseillons plutôt de suivre un des nombreux cours proposés sur le serveur via `!cours`, `!cours{langage}` et les messages épinglés dans les differents canaux.\n\nÀ noter que le mentoring gratuit ET rémunéré sont interdits ici.\n\nVous êtes bien sûr quand même les bienvenus dans les differents canaux de la communauté pour y poser des questions.","title":"À propos du mentoring (`!mentoring`)","color":3325119}}
```

### mp, vocal

```markdown
>>> ### L'aide en message privé (`!mp`, `!vocal`)

Sur Not a Name, on ne préconise ni l'aide en message privé ni l'aide en vocal. Votre problème est peut-être partagé par un autre membre, ou votre question peut en intéresser d'autres. De plus, si une unique personne vous aide et que sa façon de faire est déconseillée, vous vous retrouverez avec d'autres problèmes sur les bras ; là ou une multitude d'autres membres auraient souligné ces mauvaises pratiques.
```

```json
{"embed":{"description":"Sur Not a Name, on ne préconise ni l'aide en message privé ni l'aide en vocal. Votre problème est peut-être partagé par un autre membre, ou votre question peut en intéresser d'autres. De plus, si une unique personne vous aide et que sa façon de faire est déconseillée, vous vous retrouverez avec d'autres problèmes sur les bras ; là ou une multitude d'autres membres auraient souligné ces mauvaises pratiques.","title":"L'aide en message privé et en vocal (!mp, !vocal)","color":8388350}}
```

### recrutement

```markdown
>>> ### 3. La publicité, la présentation des projets et les messages de recrutements sont soumis à une règlementation accrue. (`!recrutement`)

Il existe des salons dédiés à ces messages et l'accès à ces salons est modéré par le staff. Tout message à tendance publicitaire ou de recrutement envoyé en dehors de ces salons ou par messages privés est interdit. Voir la section *Les salons modérés* des [#guidelines](<https://discord.com/channels/323076998576603137/860920579154772018>)
```

```json
{"embed":{"description":"Il existe des salons dédiés à ces messages et l'accès à ces salons est modéré par le staff. Tout message à tendance publicitaire ou de recrutement envoyé en dehors de ces salons ou par messages privés est interdit. Voir la section *Les salons modérés* des [#guidelines](<https://discord.com/channels/323076998576603137/860920579154772018>)","title":"3. La publicité, la présentation des projets et les messages de recrutements sont soumis à une règlementation accrue. (`!recrutement`)","color":8355584}}
```

### salon

```markdown
>>> Vous ne voyez pas le canal indiqué par les autres utilisateurs ? Voici la marche à suivre : <https://discordapp.com/channels/323076998576603137/699260551758610545/699265804994215997>
```

### scraping / webscraping

```markdown
>>> ### :spider_web: Web-scraping (`!scraping`, `!webscraping`)

Le scraping de données est la pratique de programmatiquement télécharger des données depuis un site. Il est possible de scraper en forgeant des requêtes HTTP ou bien en automatisant un navigateur web.

Le scraping n'est pas correctement couvert par un cadre légal. Sur NaN, nous n'autorisons le web-scraping que lorsque celui-ci peut s'effectuer dans le respect strict des conditions d'utilisation du site en question. En d'autres termes, lorsqu'un site propose une API et que vous voulez interagir avec ce site : vous *devez* utiliser cette API.

Toute demande d'aide concernant le web-scraping doit être accompagné d'une référence vers le passage qui autorise le scraping dans les CGU du site. À défaut, la demande d'aide tombera sous la règle concernant le respect de la loi et sera classée sans suite.

Plus d'informations sur l'état du cadre légal du web-scraping : <https://lexing.be/le-scraping-est-il-legal/>.
```

```json
{"embed":{"title":"Web-scraping","color":65024,"description":"Le scraping de données est la pratique de programmatiquement télécharger des données depuis un site. Il est possible de scraper en forgeant des requêtes HTTP ou bien en automatisant un navigateur web.\n\nLe scraping n'est pas correctement couvert par un cadre légal. Sur NaN, nous n'autorisons le web-scraping que lorsque celui-ci peut s'effectuer dans le respect strict des conditions d'utilisation du site en question. En d'autres termes, lorsqu'un site propose une API et que vous voulez interagir avec ce site : vous *devez* utiliser cette API.\n\nToute demande d'aide concernant le web-scraping doit être accompagné d'une référence vers le passage qui autorise le scraping dans les CGU du site. À défaut, la demande d'aide tombera sous la règle concernant le respect de la loi et sera classée sans suite.\n\nPlus d'informations sur l'état du cadre légal du web-scraping : <https://lexing.be/le-scraping-est-il-legal/>."}}
```

### gpt

```markdown
>>> ### :robot: Les réponses générées par IA (`!gpt` `!chatgpt`)

L'intelligence artificielle étant devenue largement accessible au public, un grand nombre de personnes sont tentées de poser leurs questions techniques à ces programmes en pensant obtenir une réponse fiable. Ce n'est pas une bonne idée, les réponses données par ces programmes sont loin d'être fiables et peuvent induire en erreur les débutants. Un certain nombre d'erreurs difficiles à déceler aux premiers abords peuvent se glisser dans une réponse globalement bien rédigée, donnant l'illusion d'une réponse valable et de bonne qualité, mais qui dans la pratique peut avoir des effets négatifs sur les projets qui se baseront dessus.
De plus, nous vous rappelons que NaN est une serveur __communautaire__, les gens qui posent des questions et demandent de l'aide doivent pouvoir discuter avec des humains qui seront en capacité de comprendre leurs besoins, le serveur n'a pas vocation à se transformer en une sorte de chatbot géant ou ne seraient échangées plus que des réponses générées automatiquement...

Pour ces raisons, il est **interdit** d'utiliser ChatGPT ou toute autre IA générative pour répondre aux questions des membres.

Pour plus d'informations à ce sujet, voir par exemple la [Politique de Stack Overflow](<https://stackoverflow.com/help/ai-policy>)
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
