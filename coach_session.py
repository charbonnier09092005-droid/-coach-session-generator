#!/usr/bin/env python3
"""
Coach Session Generator
------------------------
Génère une séance d'entraînement de football complète et aléatoire,
adaptée à une catégorie d'âge et une durée donnée.

Usage:
    python coach_session.py --category U15 --duration 90
    python coach_session.py -c U18 -d 75 --theme "jeu de transition"
"""

import argparse
import random
import textwrap

ECHAUFFEMENTS = [
    "Course active + mobilisation articulaire (8 min)",
    "Jeu de passes en carré avec 2 touches max (8 min)",
    "Rondo 4v2 en espace réduit (10 min)",
    "Activation neuromusculaire + gammes techniques (8 min)",
    "Petits jeux de possession 3v3 sur 4 zones (10 min)",
]

TECHNIQUE = [
    "Ateliers de conduite de balle en slalom + finition (15 min)",
    "Exercice de passes courtes en mouvement, triangles tournants (15 min)",
    "Travail de contrôle orienté sous pression légère (15 min)",
    "Duels 1v1 attaquant/défenseur avec zone de but (15 min)",
    "Centres-tirs depuis les couloirs (15 min)",
]

TACTIQUE = [
    "Bloc équipe : transition défense-attaque en 8v8 (20 min)",
    "Situation de jeu réduit 5v5 avec consignes de pressing (20 min)",
    "Travail du hors-jeu et ligne défensive à 4 (20 min)",
    "Jeu à thème : conservation puis verticalisation rapide (20 min)",
    "Mise en place d'un système offensif en zone haute (20 min)",
]

OPPOSITION = [
    "Match à thème sur demi-terrain (20 min)",
    "Match libre avec contraintes (2 touches max) (20 min)",
    "Opposition avec zones bonus pour le jeu extérieur (20 min)",
    "Petit match 8v8 avec objectif tactique du jour (20 min)",
]

RETOUR_AU_CALME = [
    "Étirements + retour au calme collectif (5 min)",
    "Discussion sur les points clés de la séance (5 min)",
    "Étirements individuels + debrief rapide (5 min)",
]


def generate_session(category: str, duration: int, theme: str | None) -> str:
    random.seed()
    blocs = [
        ("Échauffement", random.choice(ECHAUFFEMENTS)),
        ("Bloc technique", random.choice(TECHNIQUE)),
        ("Bloc tactique", random.choice(TACTIQUE)),
        ("Opposition", random.choice(OPPOSITION)),
        ("Retour au calme", random.choice(RETOUR_AU_CALME)),
    ]

    header = f"Séance d'entraînement — Catégorie {category} — Durée cible : {duration} min"
    if theme:
        header += f" — Thème : {theme}"

    lines = [header, "=" * len(header), ""]
    for i, (nom, contenu) in enumerate(blocs, start=1):
        lines.append(f"{i}. {nom}")
        lines.append(textwrap.indent(contenu, "   "))
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Génère une séance d'entraînement de football aléatoire."
    )
    parser.add_argument(
        "-c", "--category",
        default="U15",
        help="Catégorie d'âge (ex: U9, U13, U15, U18, Senior). Défaut: U15",
    )
    parser.add_argument(
        "-d", "--duration",
        type=int,
        default=90,
        help="Durée totale visée en minutes. Défaut: 90",
    )
    parser.add_argument(
        "-t", "--theme",
        default=None,
        help="Thème optionnel de la séance (ex: 'pressing haut')",
    )
    args = parser.parse_args()

    print(generate_session(args.category, args.duration, args.theme))


if __name__ == "__main__":
    main()
