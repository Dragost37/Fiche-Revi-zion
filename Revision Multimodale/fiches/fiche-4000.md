# Fiche 4000

## VISU
- **Perception**: capacite couleur variable; memoire auditive > visuelle.
- **Variables visuelles (~8)**: position, taille, forme, valeur/couleur, orientation, texture (souvent + mouvement/saturation).
- **Fitts**: temps de pointage depend D et W.
- **Pipeline**: acquisition -> traitement/filtrage -> mapping variables -> rendu -> affichage; activite utilisateur peut agir sur toutes les etapes.
- **Strategies**: fonctions de transfert; reduction taille + quantite combinables; navigation/zoom pour explorer.
- **Donnees**: table, liste, grille, geometrie, graphe reseau/arbre; pas toutes en grille reguliere; dimensions != nb pixels.
- **Mantra Shneiderman**: overview first, zoom/filter, details on demand.
- **Focus+context vs overview+details**: focus+context = detail+contexte simultane; overview+details = vue globale puis detail separe.

## XR
- **XR/MR**: fusion reel/virtuel.
- **VR**: monde artificiel immersif.
- **AR**: surcouche d'info au reel; telepresence = etendre capacites sensori-motrices a distance.
- **Systeme immersif**: Input -> App -> Rendering -> Display.
- **Modalites**: visuel, audio, haptique, mouvement, capteurs, interaction (geste/voix/controleur/regard).
- **HMD**: 3DoF/6DoF; handheld AR.
- **Types AR**: marker/target-based, markerless/targetless (vision-based), location-based.

## Multimodalite
- **Entrees + sorties**: multimodales; fusion/fission.
- **GUI(WIMP) vs MUI**: flux unique vs multiples; atomique/deterministe vs continu/proba; sequentiel vs parallele; centralise vs distribue.

## Affordances/signifiants
- **Affordance**: actions possibles; **signifiant**: ou/comment agir.
- **MR**: cognition spatiale (occlusion/collision, profondeur), interaction, feedback.
- **Interaction**: selection/manipulation/relachement + feedback.

## Fusion multimodale
- **Early fusion (features)** vs **late fusion (decision)**.
- **Ambiguites**: cible, lexicale, temporelle, gap.
- **Criteres**: choix modalites, temps reponse, robustesse.

## Occlusion AR
- **Principe**: virtuel occulte reel -> meme repere; z-buffer.
- **Problemes**: ordre/X-ray/transparence.
- **Approches**: model-based vs reconstructive (depth) + hybrides.

## Pointage/selection 3D
- **Techniques**: main virtuelle, ray casting, image plane, volume.
- **Modele impulsion initiale**: balistique + corrections.
- **DoF**: ray casting 5, occlusion selection 2, ray from eye 2; mismatch main-oeil.
- **Espaces**: visuel/moteur/controle; etendre/decoupler; clutching.
- **Facteurs**: env/outils/hardware/utilisateur.

## Navigation
- **Joystick**: + controle; - sickness/presence.
- **Teleportation**: + effort bas; - desorientation.
- **Human joystick**: + intuitif; - effort/espace.
- **Redirected walking**: rotation virtuelle imperceptible; HMD 6DoF + tracking + modele piece.
- **Gains**: translation 0.86-1.26; rotation 0.67-1.24; courbure G=0.045 (~13 deg/5 m, rayon 22 m).
- **Comparatif**: sickness joystick > redirected > teleport; presence redirected > teleport > joystick.

## Motion sickness
- **Causes**: conflit sensoriel, latence, instabilite posturale, facteurs bio; 3DoF vs 6DoF.
- **Eval**: SSQ + physio.
- **Solutions**: reduire FOV/rotations, teleportation, assis, reduire latence.

## UX
- **Immersion**: contingences sensorimotrices; **presence**: place illusion; **plausibility**: coherence evenements/sensations.
- **Immersion (techno)** cadre **presence (psy)**.
- **Uncanny valley**.
- **Eval**: ITQ (jeu/focus/implication), SUS, NASA-TLX, SSQ + physio/comportement.

## Embodiment
- **Definition**: se sentir dans un corps virtuel.
- **SoE**: self-location, agency, ownership.
- **Rubber Hand Illusion**: integration multisensorielle.

## CSCW (trefle des collecticiels)
- **Communication** (echanges), **Coordination** (roles/taches/temps), **Production** (co-creation).
