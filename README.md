# ⚽ Coach Session Generator

Un petit outil en ligne de commande qui génère instantanément une **séance d'entraînement de football complète**, adaptée à une catégorie d'âge, une durée et un thème.

Idéal pour les éducateurs qui manquent de temps ou d'inspiration avant une séance, ou pour varier ses contenus.

## 🚀 Utilisation rapide

```bash
git clone https://github.com/<ton-pseudo>/coach-session-generator.git
cd coach-session-generator
python3 coach_session.py --category U15 --duration 90
```

Exemple de sortie :

```
Séance d'entraînement — Catégorie U15 — Durée cible : 90 min
==============================================================

1. Échauffement
   Rondo 4v2 en espace réduit (10 min)

2. Bloc technique
   Ateliers de conduite de balle en slalom + finition (15 min)

3. Bloc tactique
   Bloc équipe : transition défense-attaque en 8v8 (20 min)

4. Opposition
   Match à thème sur demi-terrain (20 min)

5. Retour au calme
   Étirements + retour au calme collectif (5 min)
```

## 🎛️ Options

| Option | Description | Défaut |
|---|---|---|
| `-c`, `--category` | Catégorie d'âge (U9, U13, U15, U18, Senior...) | `U15` |
| `-d`, `--duration` | Durée cible en minutes | `90` |
| `-t`, `--theme` | Thème libre de la séance | aucun |

## 💡 Pourquoi ce projet ?

Les éducateurs sportifs passent souvent du temps à structurer leurs séances de zéro. Cet outil propose une base aléatoire mais cohérente (échauffement → technique → tactique → opposition → retour au calme) qu'on peut ensuite ajuster.

## 🤝 Contribuer

Les contributions sont bienvenues ! Idées d'amélioration :
- Ajouter de nouveaux exercices dans chaque catégorie
- Export PDF ou Markdown de la séance
- Génération de plusieurs séances sur un cycle (semaine/mois)
- Interface web simple

N'hésite pas à ouvrir une issue ou une pull request.

## 📄 Licence

MIT — libre d'utilisation, de modification et de distribution.
