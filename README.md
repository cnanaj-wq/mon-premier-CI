# Mon premier projet CI

Projet d'apprentissage de Python, des tests automatisés,
de Git et de GitHub Actions.

## Objectif

Vérifier qu'un nom est renseigné avant de l'accepter.

La fonction `verifier_nom` reçoit du texte ou `None`.

| Entrée | Résultat attendu |
|---|---|
| `"Dupont"` | Renvoie `True` |
| `""` | Lève une `ValueError` |
| `"   "` | Lève une `ValueError` |
| `None` | Lève une `ValueError` |

## Prérequis

- Python 3.12, version utilisée dans la CI.
- Git pour récupérer le projet et gérer son historique.

Les tests utilisent `unittest`, inclus dans Python.
Aucun paquet Python supplémentaire n'est nécessaire.

## Récupérer le projet

```powershell
git clone https://github.com/cnanaj-wq/mon-premier-CI.git
cd mon-premier-CI
```

Ces commandes servent à créer une nouvelle copie locale du projet.

## Lancer les tests

Depuis le dossier du projet :

```powershell
python test_students.py -v
```

Le résultat attendu est :

```text
Ran 4 tests in ...

OK
```

La durée d'exécution peut varier.

## Organisation du projet

- `students.py` : fonction de validation des noms.
- `test_students.py` : quatre tests automatisés.
- `.gitignore` : règles pour ignorer les fichiers locaux inutiles à l'historique.
- `.github/workflows/ci.yml` : configuration de GitHub Actions.
- `README.md` : présentation et mode d'emploi du projet.

## Intégration continue

Le workflow `CI Python` se lance à chaque push sur `main`.

Il effectue trois étapes sur une machine Ubuntu :

1. Récupérer le code du dépôt.
2. Préparer Python 3.12.
3. Exécuter les quatre tests.

Si un test échoue, le job est signalé en échec.

Les résultats sont disponibles dans
[l'onglet Actions](https://github.com/cnanaj-wq/mon-premier-CI/actions).

## Limites actuelles

- Les tests couvrent les quatre cas décrits dans ce document.
- Une CI réussie ne garantit pas l'absence de tous les bugs.
- Aucun déploiement n'est configuré.
- La protection de la branche `main` n'a pas encore été configurée.