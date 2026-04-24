db = db.getSiblingDB('blog_db');

if (!db.getCollectionNames().includes('posts')) {
  db.createCollection('posts');
}

db.runCommand({
  collMod: 'posts',
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['titre', 'auteur', 'vues'],
      properties: {
        _id: { bsonType: 'objectId' },
        titre: { bsonType: 'string', minLength: 3 },
        auteur: { bsonType: 'string', minLength: 1 },
        vues: { bsonType: 'int', minimum: 0 },
        contenu: { bsonType: 'string' },
        dateCreation: { bsonType: 'date' }
      },
      additionalProperties: false
    }
  }
});

const articles = [
  { titre: 'Frederic', auteur: 'Frederic', vues: 358, contenu: 'Fred ou Rick ?', dateCreation: new Date('2026-01-12') },
  { titre: 'Evan', auteur: 'Evan', vues: 917, contenu: 'un mec qui est cool', dateCreation: new Date('2026-02-03') },
  { titre: 'Sacha', auteur: 'Sacha', vues: 753, contenu: 'meilleur frontend developer', dateCreation: new Date('2026-02-18') },
  { titre: 'Ugo', auteur: 'Ugo', vues: 236, contenu: 'joueur de brawl stars', dateCreation: new Date('2026-03-05') },
  { titre: 'Zayd', auteur: 'Zayd', vues: 9802, contenu: 'meilleur backend developer', dateCreation: new Date('2026-03-22') }
];

db.posts.deleteMany({});
db.posts.insertMany(articles);

