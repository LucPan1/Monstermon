tables = {
    'Espece': {
        'columns': [
            ('espece_id', 'INT PRIMARY KEY AUTO_INCREMENT'),
            ('nom', 'VARCHAR(100) NOT NULL')
        ],
        'values': [
        (1, 'Fluffernox'),
        (2, 'Glacéphalosaurus'),
        (3, 'Pluminsecte'),
        (4, 'Bulbosarbre'),
        (5, 'Aquastruth'),
        (6, 'Pyrovolcanix'),
        (7, 'Ventisphère'),
        (8, 'Cristalpuma'),
        (9, 'Sylvabulle'),
        (10, 'Gravifouetteur')
]
    },
    'Dresseur': {
        'columns': [
            ('dresseur_id', 'INT PRIMARY KEY AUTO_INCREMENT'),
            ('nom', 'VARCHAR(50) NOT NULL'),
            ('prenom', 'VARCHAR(50) NOT NULL'),
            ('genre', 'ENUM("M", "F") NOT NULL'),
            ('idProfesseur', 'INT'),
            ('EstProfesseur', 'BOOLEAN NOT NULL'),
            ('FOREIGN KEY (idProfesseur)', 'REFERENCES Dresseur(dresseur_id)')
        ],
        'values': [
    (1, 'Anderson', 'Ethan', 'M', None, 'Oui'),
    (2, 'Martinez', 'Daniel', 'M', 1, 'Non'),
    (3, 'Johnson', 'Olivia', 'F', None, 'Oui'),
    (4, 'Nguyen', 'Isabella', 'F', 11, 'Non'),
    (5, 'Smith', 'Michael', 'M', None, 'Oui'),
    (6, 'García', 'Michel', 'M', 12, 'Non'),
    (7, 'Williams', 'James', 'M', None, 'Non'),
    (8, 'Rodriguez', 'Lucas', 'M', None, 'Non'),
    (9, 'Brown', 'Sophia', 'F', 5, 'Non'),
    (10, 'Patel', 'Harper', 'F', 3, 'Non'),
    (11, 'Clark', 'Mia', 'F', None, 'Oui'),
    (12, 'Hall', 'Charlotte', 'F', None, 'Oui')
]
    },
    'Type': {
        'columns': [
            ('type_id', 'INT PRIMARY KEY AUTO_INCREMENT'),
            ('nom', 'VARCHAR(50) NOT NULL')
        ],
        'values': [
            (1, 'feu'),
            (2, 'eau'),
            (3, 'air'),
            (4, 'terre')
        ]
    },
    'Monster': {
        'columns': [
            ('monster_id', 'INT PRIMARY KEY AUTO_INCREMENT'),
            ('nom', 'VARCHAR(50) NOT NULL'),
            ('pointExp', 'INT NOT NULL'),
            ('pointVie', 'INT NOT NULL'),
            ('poids', 'INT NOT NULL'),
            ('espece_id', 'INT'),
            ('taille', 'INT NOT NULL'),
            ('pointPuissance', 'INT NOT NULL'),
            ('type_id', 'INT'),
            ('niveau', 'INT NOT NULL'),
            ('capturee', 'varchar(5) NOT NULL'),
            ('dateCapture', 'DATE'),
            ('idDresseur', 'INT'),
            ('FOREIGN KEY (espece_id)', 'REFERENCES Espece(espece_id)'),
            ('FOREIGN KEY (type_id)', 'REFERENCES Type(type_id)'),
            ('FOREIGN KEY (idDresseur)', 'REFERENCES Dresseur(dresseur_id)')
        ],
        'values': [
            (1, 'Grizzlor', 1, 1000, 200, 20, 90, 150, 1, 10, True, '2022-12-14', 2),
            (2, 'Azurika', 2, 2451, 100, 70, 70, 150, 1, 5, False, None, None),
            (3, 'Crépulor', 1, 8402, 200, 80, 80, 250, 2, 3, False, None, None),
            (4, 'Vortexar', 2, 1203, 300, 90, 90, 350, 3, 6, True, '2023-07-14', 3),
            (5, 'Gorgonix', 3, 8321, 400, 100, 100, 400, 4, 10, True, '2023-06-28', 5),
            (6, 'Zéphirium', 3, 893, 500, 100, 100, 500, 5, 5, False, None, 4),
            (7, 'Krypthona', 2, 193, 100, 30, 40, 200, 1, 3, False, None, 10),
            (8, 'Glaciarax', 3, 1893, 170, 60, 80, 300, 2, 6, True, '2022-10-19', 11),
            (9, 'Infernion', 1, 9903, 250, 100, 90, 400, 3, 6, True, '2023-01-18', 11),
            (10, 'Sylvarath', 2, 10000, 500, 150, 100, 500, 4, 6, True, '2023-03-29', 12),
            (11, 'Draconyx', 1, 9213, 100, 10, 30, 70, 1, 2, False, None, 1),
            (12, 'Abominix', 2, 9241, 180, 30, 40, 100, 2, 1, False, None, 3),
            (13, 'Hydrokhan', 4, 6000, 270, 40, 50, 200, 3, 2, False, None, None),
            (14, 'Sombrodeus', 4, 7313, 300, 45, 60, 300, 4, 5, True, '2023-09-11', 8),
            (15, 'Nébulorok', 2, 513, 500, 50, 65, 500, 5, 7, True, '2023-06-28', 8),
            (16, 'Terramorth', 3, 64, 200, 25, 90, 150, 2, 8, False, None, 8),
            (17, 'Zombalith', 1, 22, 100, 70, 50, 200, 3, 1, False, None, 7),
            (18, 'Phantasmagor', 1, 10, 500, 35, 60, 300, 4, 2, True, '2023-08-09', 9),

            (19, 'Colossinge', 1, 1000, 200, 20, 90, 150, 1, 10, True, '2022-12-14', 2),
            (20, 'Onix', 1, 1000, 200, 20, 90, 150, 1, 10, True, '2022-12-14', 2),
            (21, 'Machoc', 1, 1000, 200, 20, 90, 150, 1, 10, True, '2022-12-14', 2)
        ]
    },
    'Arene': {
        'columns': [
            ('arene_id', 'INT PRIMARY KEY AUTO_INCREMENT'),
            ('nom', 'VARCHAR(100) NOT NULL'),
            ('localisation', 'VARCHAR(100) NOT NULL'),
            ('nombrePlace', 'INT'),
            ('taille', 'INT')
        ],
        'values': [
            (1, 'Helicops', '456 Boulevard de la Fantaisie Revopolis', 25, 250),
            (2, 'Sun', '123 Rue des Etoiles Lumiereville Mystica', 5, 70),
            (3, 'Eclair', '789 Avenue des Arc-en-Ciel Feeriqueville', 500, 3000),
            (4, 'Terra', '234 Allée de l\'Aventure Arcadia Légendaville', None, None)
        ]
    },
    'Quete': {
        'columns': [
            ('quete_id', 'INT PRIMARY KEY AUTO_INCREMENT'),
            ('nomQuete', 'VARCHAR(100) NOT NULL'),
            ('localisation', 'VARCHAR(100) NOT NULL'),
            ('debut', 'DATE NOT NULL'),
            ('fin', 'DATE'),
            ('pointExGagne', 'INT NOT NULL'),
            ('estPerm', 'BOOLEAN NOT NULL')
        ],
        'values': [
            (1, "La Quête du Trésor Perdu", "123 Rue des Mystères Ombreville", '2023-04-10', '2023-04-20', 350, True),
            (2, "La Chasse aux Créatures Mythiques", "Forêt Enchantée Clairière des Lutins", '2023-06-05', None, 2000, True),
            (3, "L'Expédition dans les Profondeurs", "Cité Sous-Marine d'Abyssia Rue des Coraux", '2023-09-02', '2023-09-12', 3500, True),
            (4, "La Mission Secrète du Château Hanté", "Château Hanté de la Lune Noire; Salle des Fantômes", '2023-11-13', '2023-11-23', 7000, False),
            (5, "La Conquête du Pic de Glace", "Montagne Gelée Sommet de Cristal", '2023-12-05', '2023-12-15', 25000, True),
            (6, "La Recherche du Livre des Sortilèges", "Bibliothèque Antique; Rayon des Grimoires", '2023-10-02', None, 500, False),
            (7, "Le Mystère de la Pierre de Lune", "Forêt de Lumière Clairière des Fées", '2023-08-21', '2023-08-31', 800, False),
            (8, "La Quête du Dragon Doré", "Caverne des Dragons Antre du Gardien", '2023-06-28', None, 250, True)
        ]
    },
    'Magasin': {
        'columns': [
            ('magasin_id', 'INT PRIMARY KEY AUTO_INCREMENT'),
            ('nom', 'VARCHAR(100) NOT NULL'),
            ('localisation', 'VARCHAR(100) NOT NULL')
        ],
        'values': [
            (1, 'LumierMart', '123 Rue de la Liberté Arc-en-Cielville'),
            (2, 'EcoMonster', '456 Avenue des Songes Luneville'),
            (3, 'MoCouture', '789 Chemin de la Féeerie Flottemagie'),
            (4, 'SavSphere', '101 Rue des Nuages Crystallineville'),
            (5, 'MobiliBulle', '234 Allée des Mystères Ensorcelville'),
            (6, 'GalactiGear', '567 Boulevard de l\'Aurore Cielétincell'),
            (7, 'PlanePlantes', '890 Promenade de l\'Enchantement Brumeville'),
            (8, 'MystiMonster', '210 Avenue des Lumières Sylveclaire'),
            (9, 'RobeoMonster', '543 Rue des Étoiles Fleurétoile'),
            (10, 'ArteMonster', '876 Chemin de la Magie Auroreville')
        ]
    },
    'Vente': {
        'columns': [
            ('vente_id', 'INT PRIMARY KEY AUTO_INCREMENT'),
            ('dresseur_id', 'INT'),
            ('magasin_id', 'INT'),
            ('prix', 'INT NOT NULL'),
            ('monster_id', 'INT'),
            ('date', 'DATE NOT NULL'),
            ('FOREIGN KEY (dresseur_id)', 'REFERENCES Dresseur(dresseur_id)'),
            ('FOREIGN KEY (magasin_id)', 'REFERENCES Magasin(magasin_id)'),
            ('FOREIGN KEY (monster_id)', 'REFERENCES Monster(monster_id)')
        ],
        'values': [
            (1, 2, 1, 500, 1, '2023-01-15'),
            (2, 1, 2, 600, 2, '2023-03-22'),
            (3, 2, 4, 450, 2, '2023-05-10'),
            (4, 5, 3, 700, 1, '2023-07-18'),
            (5, 1, 1, 550, 3, '2023-09-05'),
            (6, 3, 5, 800, 4, '2023-10-30'),
            (7, 4, 2, 600, 5, '2023-12-12')
        ]
    },
    'Equipement': {
        'columns': [
            ('equipement_id', 'INT PRIMARY KEY AUTO_INCREMENT'),
            ('nom', 'VARCHAR(100) NOT NULL'),
            ('type_id', 'INT'),
            ('arene_id', 'INT'),
            ('FOREIGN KEY (type_id)', 'REFERENCES Type(type_id)'),
            ('FOREIGN KEY (arene_id)', 'REFERENCES Arene(arene_id)')
        ],
        'values': [
            (1, 'Lac', 1, '2'),
            (2, 'Fontaine', 1, '2'),
            (3, 'Pierres', 2, '4'),
            (4, 'Monuments', 3, '4')
        ]
    },
    'Evenement': {
        'columns': [
            ('evenement_id', 'INT PRIMARY KEY AUTO_INCREMENT'),
            ('nom', 'VARCHAR(100) NOT NULL'),
            ('dateDebut', 'DATE NOT NULL'),
            ('dateFin', 'DATE NOT NULL'),
            ('prix', 'INT NOT NULL'),
            ('monster_id', 'INT'),
            ('arene_id', 'INT'),
            ('FOREIGN KEY (monster_id)', 'REFERENCES Monster(monster_id)'),
            ('FOREIGN KEY (arene_id)', 'REFERENCES Arene(arene_id)')
        ],
        'values': [
            (1, "Tournoi du Poing d'Acier", '2023-04-15', '2023-04-18', 50, 3, 2),
            (2, "L'Arène des Titans", '2023-06-10', '2023-06-12', 75, 3, 3),
            (3, "La Bataille des Rois", '2023-08-20', '2023-08-20', 100, 4, 4),
            (4, "Championnat Mondial des Monsters", '2023-09-15', '2023-09-18', 200, 3, 1),
            (5, "La Guerre des Monsters", '2023-11-05', '2023-11-10', 60, 1, 2),
            (6, "Le Duel des Titan", '2023-12-08', '2023-12-11', 45, 1, 3),
            (7, "L'Ultimatum des Airs", '2023-12-01', '2024-01-05', 30, 3, 3),
            (8, "Le Carnage des Monsteurs de Feu", '2024-01-25', '2024-02-14', 150, 4, 1),
            (9, "La Grande Joute des Héros", '2024-02-12', '2024-02-20', 679, 1, 1),
            (10, "Le Choc des Éléments", '2024-03-12', '2024-04-20', 1000, 3, 2)
        ]
    },
    'Combat': {
    'columns': [
        ('combat_id', 'INT PRIMARY KEY AUTO_INCREMENT'),
        ('dateDebut', 'DATE NOT NULL'),
        ('dateFin', 'DATE NOT NULL'),
        ('evenement_id', 'INT'),
        ('FOREIGN KEY (evenement_id)', 'REFERENCES Evenement(evenement_id)')
    ],
    'values': [
        (1, '2023-10-01', '2023-10-02', 1),
        (2, '2023-11-01', '2023-11-02', 2),
        (3, '2023-07-15', '2023-07-16', 1),
        (4, '2023-08-20', '2023-08-22', 2),
        (5, '2023-09-10', '2023-09-12', 3),
        (6, '2023-10-05', '2023-10-07', 4),
        (7, '2023-11-15', '2023-11-17', 5)  
    ]
    },
}

extra_tables = {
    'participation_evenement': {
        'columns': [
            ('evenement_id', 'INT'),
            ('monster_id', 'INT'),
            ('date_participation', 'DATE NOT NULL'),
        ],
        'primary_key': ['evenement_id', 'monster_id'],
        'foreign_keys': [
        ('evenement_id', 'Evenement(evenement_id)'),
        ('monster_id', 'Monster(monster_id)')
    ],
        'values': [
            (1, 2, '2023-10-02'),
            (2, 1, '2023-11-02')
        ]
    },
        'Combat_Monster': {
            'columns': [
                ('combat_id', 'INT'),
                ('monster_id', 'INT'),
                ('resultat', 'BOOLEAN NOT NULL'),
            ],
            'primary_key': ['combat_id', 'monster_id'],
            'foreign_keys': [
            ('combat_id', 'Combat(combat_id)'),
            ('monster_id', 'Monster(monster_id)')
            ],
            'values': [
                (1, 1, True),
                (2, 2, False)
            ]
        },
        'participation_quete': {
            'columns': [
                ('monster_id', 'INT'),
                ('quete_id', 'INT'),
                ('dateDebut', 'DATE NOT NULL'),
            ],
            'primary_key': ['monster_id', 'quete_id'],
            'foreign_keys': [
            ('monster_id', 'Monster(monster_id)'),
            ('quete_id', 'Quete(quete_id)')
            ],
            'values': [
                (1, 1, '2023-09-05'),
                (2, 2, '2023-09-17')
            ]
        }
}