# Mon premier projet CI/CD

Un projet pour apprendre à **tester un changement (CI)** puis à **publier automatiquement un site (CD)** avec Python, Git et GitHub Actions.

👉 [Visiter le site](https://cnanaj-wq.github.io/mon-premier-CI/)
 · [Explorer le schéma interactif CI/CD](https://cnanaj-wq.github.io/mon-premier-CI/architecture-ci.html)

## Ce que fait le projet

La fonction `verifier_nom` vérifie qu'un nom est renseigné. Elle reçoit une chaîne de caractères ou `None`.

| Entrée | Résultat attendu |
|---|---|
| `"Dupont"` | Renvoie `True` |
| `""` | Lève une `ValueError` |
| `"   "` | Lève une `ValueError` |
| `None` | Lève une `ValueError` |

Les quatre tests Python vérifient ces cas. Le site publié présente le parcours CI/CD : il n'exécute pas le programme Python dans un serveur.

## CI et CD : deux rôles complémentaires

| Partie | Question | Job |
|---|---|---|
| **CI — intégration continue** | Le changement passe-t-il les contrôles ? | `tests` |
| **CD — déploiement continu** | Peut-on publier la version validée ? | `deploy` |

La CI reste présente : la CD vient après elle. La fusion de la PR est humaine ; la publication qui suit la réussite des contrôles sur `main` est automatique.

## Parcours complet

1. Créer une branche, modifier les fichiers, faire un commit puis un push.
2. Ouvrir une pull request vers `main`.
3. GitHub exécute le job `tests`. Sur la PR, `deploy` est ignoré (`Skipped`).
4. La protection de `main` exige une PR et la réussite du contrôle `tests`. Une CI rouge bloque la fusion.
5. Fusionner la PR : le push résultant sur `main` relance les contrôles.
6. Si ces contrôles réussissent, le job `deploy` publie le contenu de `docs` sur GitHub Pages.
7. Ouvrir le site et vérifier l'accueil ainsi que le schéma interactif.

## Le workflow CI/CD

La configuration se trouve dans `.github/workflows/ci.yml`, sous le nom **CI/CD Python** dans [l'onglet Actions](https://github.com/cnanaj-wq/mon-premier-CI/actions).

### CI : le job `tests`

Sur une machine Ubuntu 24.04, avec une limite de cinq minutes :

1. Récupérer le code avec `actions/checkout`.
2. Préparer Python 3.12.
3. Exécuter `python test_students.py -v`.
4. Vérifier que `docs/index.html` et `docs/architecture-ci.html` existent et ne sont pas vides.

### CD : le job `deploy`

Deux conditions commandent la publication :

```yaml
needs: tests
if: github.event_name == 'push' && github.ref == 'refs/heads/main'
```

- `needs: tests` impose d'attendre la réussite du job de contrôle.
- `if` réserve la publication aux événements `push` sur `main`.

Le job récupère le code sur sa propre machine, prépare GitHub Pages, transmet un **artefact** nommé `github-pages` contenant `docs`, puis publie ce paquet. Sa limite est de dix minutes.

Les permissions `pages: write` et `id-token: write` sont limitées au job de déploiement. Le groupe de concurrence `github-pages` empêche deux publications de ce workflow de s'exécuter simultanément, sans annuler celle déjà en cours.

Dans **Settings → Pages**, la source doit être **GitHub Actions** : c'est ce workflow qui décide de publier.

| Situation | Tests | Publication |
|---|---|---|
| PR vers `main`, contrôles réussis | Réussite | Ignorée |
| PR vers `main`, contrôle en échec | Échec, fusion bloquée | Ignorée |
| Push sur `main`, contrôles réussis | Réussite | Exécutée |
| Push sur `main`, contrôle en échec | Échec | Ignorée ; site existant conservé |

Si le job `deploy` échoue, consulter son journal : des tests verts ne suffisent pas à prouver une publication réussie.

## Prérequis et installation

- Python 3.12, utilisé par les tests du workflow CI/CD.
- Git pour récupérer le projet et gérer son historique.
- `unittest` est inclus dans Python : aucun paquet Python supplémentaire à installer.

Pour créer une nouvelle copie locale :

```powershell
git clone https://github.com/cnanaj-wq/mon-premier-CI.git
cd mon-premier-CI
```

## Lancer les tests localement

Depuis le dossier du projet :

```powershell
python test_students.py -v
```

Résultat attendu : `Ran 4 tests`, puis `OK`. Cette commande teste le code Python ; elle ne publie pas le site.

## Organisation du projet

| Fichier | Rôle |
|---|---|
| `students.py` | Validation des noms |
| `test_students.py` | Quatre tests automatisés |
| `.github/workflows/ci.yml` | Workflow CI/CD : contrôles puis publication |
| `docs/index.html` | Accueil du site |
| `docs/architecture-ci.html` | Schéma interactif CI/CD autonome |
| `diagrams/ci-cd.workflow.json` | Source Archify modifiable du schéma |
| `.gitignore` | Exclusion des fichiers locaux inutiles à l'historique |
| `README.md` | Présentation et mode d'emploi |

## Schéma interactif CI/CD

👉 [Ouvrir le schéma interactif](https://cnanaj-wq.github.io/mon-premier-CI/architecture-ci.html)

- **Flux bleu-gris : CI**, de l'événement aux contrôles.
- **Flux vert / turquoise : CD**, de l'autorisation de publier à la page livrée.
- **Flux rose : échec**, arrêt de la chaîne avant publication.
- Cliquer sur un nœud permet d'explorer ses relations et ses sources.
- Les vues guidées distinguent CI et CD. Signal Flow change la présentation ; Live anime les connexions.

L'animation est pédagogique : elle ne lance aucun test et ne montre pas l'état réel de GitHub. Les commandes du lecteur sont partiellement en anglais. Les chemins historiques `ci.yml` et `architecture-ci.html` sont conservés pour maintenir les liens existants.

## Limites actuelles

- Les tests couvrent les quatre cas décrits ; ils ne prouvent pas l'absence de tous les bugs.
- Le contrôle des HTML vérifie leur présence et leur taille, pas leur rendu ni tous leurs liens.
- Seul le site statique est déployé. Aucun serveur Python ni base de données n'est publié.
- Les règles de protection de `main` se configurent dans GitHub ; elles ne sont pas définies dans le YAML.
- Le schéma doit être actualisé lorsque le workflow évolue. Ses liens de source pointent vers la version du workflow utilisée pour le construire.
