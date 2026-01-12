# FICHE COMPLETE - Techniques d'Interaction et Multimodalite

## Visualisation de l'information

- Perception: capacite de perception des couleurs variable selon les utilisateurs.
- Variables visuelles (Bertin): position, taille, forme, valeur/luminosite, couleur (teinte), orientation, texture, (souvent ajoute: mouvement/saturation).
- Memoire: la memoire auditive persiste plus longtemps que la memoire visuelle.
- Fitts: temps de pointage depend de la distance D et de la largeur W.
- Pipeline de visualisation: acquisition -> traitement/filtrage -> mapping sur variables visuelles -> rendu -> affichage; l'activite utilisateur peut impacter toutes les etapes.
- Strategies: fonctions de transfert pour adapter les donnees; reduction de taille + reduction de quantite peuvent se combiner; navigation/zoom pour explorer l'espace d'information.
- Donnees: table, liste, grille, geometrie, graphe (reseau), graphe (arbre); pas toutes les techniques sont des grilles regulieres; dimensions != nombre de pixels.
- Mantra de Shneiderman: overview first, zoom/filter, details on demand.
- Focus+context vs overview+details: focus+context montre detail + contexte simultanement (ex. fisheye); overview+details separe vue globale et detail.

## XR / VR / AR et continuum

- XR/MR: fusion du reel et du virtuel; objets reels/virtuels coexistent et sont interactifs.
- Continuum realite-virtualite (Milgram).
- VR: monde entierement artificiel; immersion totale.
- AR: information numerique injectee/superposee au reel.
- Telepresence: etendre les capacites sensori-motrices et de resolution de problemes a distance.
- Systeme immersif: Input (donnees utilisateur) -> Application (logique non rendue) -> Rendering (transfo representation -> experience) -> Display (representation physique).

## Modalites et interfaces

- Modalites: visuel, audio, haptique, mouvement, capteurs, interaction (gestes, voix, controleurs, regard).
- HMD: connecte ou autonome; 3DoF vs 6DoF; FOV env. 110 deg H / 95 deg V.
- Handheld: 6DoF; AR/virtuality; mobile AR et smart glasses.
- Types d'AR: marker/target-based, markerless/targetless (vision-based), location-based (indoor tracking/GPS).

## Multimodalite

- Definition: interaction avec environnement physique/virtuel via modes naturels.
- Multimodalite intervient a l'entree (inputs multimodaux) et a la sortie (outputs multimodaux).
- Fusion et fission multimodales dans la boucle humain-machine.
- GUI (WIMP) vs MUI: flux unique vs multiples; atomique/deterministe vs continu/probabiliste; sequentiel vs parallele; centralise vs distribue.

## Affordances et signifiants (MR)

- Affordance: actions possibles; relation capacites utilisateur/proprietes objet.
- Signifiant: indique ou/comment agir; rend l'affordance perceptible.
- MR: cognition spatiale (occlusion/collision, profondeur), interaction, feedback.
- Interaction: selection, manipulation, relachement; feedback graphique/audio/haptique.
- Principes: selection (indication + feedback), manipulation (attachement, position/orientation, feedback), relachement (indication + position finale).

## Fusion multimodale

- Early fusion (feature/reconnaissance): modalites = features integrees dans un modele.
- Late fusion (semantique/decision): fusion par dictionnaire/choix.
- Ambiguites: cible, lexicale, temporelle, gap.
- Criteres: choix modalites, temps de reponse, robustesse a l'ambiguite.

## Occlusion en AR/MR

- Par defaut, les objets virtuels occultent le reel -> besoin d'un cadre commun.
- Probleme d'occlusion 3D: ordre, X-ray, transparence; z-buffer pour profondeur.
- Approche model-based: modele du monde + alignement.
- Approche reconstructive: cameras profondeur + surfaces lisses.
- Approche hybride (ex. modele de main + profondeur).

## Pointage et selection 3D

- Opportunites: gestes naturels, plus de DoF, expressivite.
- Defis: dexterite, indices visuels, contraintes physiques.
- Techniques: main virtuelle (naturel mais limite), ray casting (bras etendu; precision/occlusion), image plane (visibilite; fatigue/vergence), selection volumique (grandes zones mais complexe).
- Fitts: temps depend de D et W.
- Modele d'impulsion initiale: mouvement balistique + corrections.
- DoF: ray casting 5 DoF; occlusion selection 2 DoF; ray casting depuis l'oeil 2 DoF; mismatch main-oeil.
- Espaces: visuel, moteur (physique), controle (transfo du moteur). Etendre/decoupler; deplacer via clutching.
- Facteurs: environnement (geometrie, distance, densite), outil (DoF, portee, ergonomie), materiel (latence, bruit), utilisateur (fatigue, preference).

## Mouvement et navigation en VR

- Motivations: presence, interactions riches, plus de DoF, immersion credible.
- Defis: synchro capteurs, fatigue, espace limite, mapping reel/virtuel, latence/motion sickness.
- Chaises/tapis: haut de gamme, couteux, usages limites (YawVR/RotoVR, Virtuix Omni/Virtualizer, Infinadeck).
- Joystick: + controle, peu de fatigue; - sickness, presence faible, collisions.
- Point-and-teleport: pointer + orientation; + effort reduit, moins de sickness; - desorientation, precision.
- Human joystick: + intuitif; - effort/precision, espace limite, cout.
- Redirected walking: rotation virtuelle imperceptible pour devier la marche reelle; HMD 6DoF + modele piece + tracking.
  - Gains: translation 0.86-1.26; rotation 0.67-1.24; courbure G=0.045 (~13 deg/5 m, rayon 22 m).
  - Combiner gains -> marche infinie.
  - Comparatif: sickness joystick > redirected > teleport; presence redirected > teleport > joystick.

## Motion sickness

- Frequence elevee (~25%), conflit sensoriel, surtout mouvement lateral.
- Causes: equipement (3DoF vs 6DoF, controleur), latence, instabilite posturale, facteurs bio (age, sante).
- Evaluation: SSQ, tests stabilite posturale, mesures physiologiques (FC, clignement, sudation).
- Solutions: reduire FOV, Nasum Virtualis, reduire rotations, teleportation, assis, reduire latence.

## Fission multimodale (sorties)

- Role: selection/structuration contenu; selection modalites; coordination sorties.
- Selection contenu: schema (predicats) ou planification (effets, preconditions, contraintes).
- Selection modalites: linguistique vs non; arbitraire vs non; analogique vs non; statique vs dynamique; modalite physique (graphique, acoustique, haptique).
- Coordination: layout physique, coordination temporelle (Allen), expressions referentielles.
- Ref. multimodales vs cross-modales; alignement temps/lieu; acces representation interne.

## Audio immersif

- Composantes: son source, propagation (RIR), HRTF, synthese binaurale.
- Propagation: reflexion, transmission, diffraction; facteurs obstacles, materiaux, environnement.
- Plausibilite binaurale: ergonomie casque, indices spectraux individuels, mouvements tete (latence), acoustique salle.

## Haptique

- Recepteur: cutanes (mecano, douleur, chaud/froid) + kinesthesiques.
- Interfaces: handheld, wearable (electrotactile, gilet, exosquelette, Peltier), encountered (bras robot, drones), props physiques, mid-air (ultrasons).
- Defis: vocabulaire, contraintes spatio-temporelles, poids/ergonomie.

## Accessibilite (basse vision)

- Deficience visuelle non corrigible (ex. DMLA).
- Difficultes VR: distance, interaction, eclairage.
- Augmentations: grossissement, luminosite/contraste, recoloration, edge enhancement.
- Feedback: visuel (distance, highlight, guideline), audio (TTS, description), haptique, audio-visuel, feedback d'action.

## UX en XR: immersion, presence, plausibilite

- Immersion = support contingences sensorimotrices (FOV, resolution, stereo, rendu tete, eclairage, frame rate; extensiveness, matching, surroundness, vividness, interactability, plot).
- Presence (Place Illusion) = sentiment d'etre la.
- Plausibility Illusion = coherence evenements/sensations.
- Immersion (techno) cadre presence (psy); uncanny valley possible.
- Evaluation: questionnaires (ITQ jeu/focus/implication; SUS, NASA-TLX, UTAUT2, SSQ), mesures physiologiques, comportements.

## Embodiment

- Definition: ressentir un corps virtuel comme son propre corps.
- Rubber Hand Illusion: integration multisensorielle -> appropriation d'un membre artificiel.
- SoE: self-location, agency, ownership.
- Evaluation SoE: questionnaires + estimation position/taille + reponses physiologiques.
- Illusion des six doigts; avatars (enfant, autre race/genre, non-humain) -> effets perceptifs/comportementaux.

## Capture de mouvement et volumetrique

- Objectifs: comportements naturels, realisme, ergonomie; applis divertissement/sante/robotique.
- Defis: precision (drift), latence, occlusion, cout, ergonomie, post-traitement.
- Technologies: RGB(D), inertiel, optique (marqueurs), volumetrique (multi-cameras).
- Mocap optique: IR 8-16 cameras; calibration; pipeline (debruitage -> 2D -> ID -> 3D -> squelette -> edition). + precision; - cout, post-traitement, occlusion.
- Mocap inertiel: gyros/acceleros; calibration + cleanup; + grande zone, pas d'occlusion; - bruit, drift, pas capture visage.
- Volumetrique: reconstruction 3D/point clouds, Gaussian splatting; + realisme, confort; - tres cher, post-traitement.
- Comparaison: realisme, temps reel, cout, confort, liberte, programmabilite, durabilite.
- Autres: capture visage (app), gestes (camera HMD).

## CSCW / trefle des collecticiels

- Communication: echanges et partage d'information.
- Coordination: organisation des roles, taches, temps.
- Production: co-creation de l'artefact.
