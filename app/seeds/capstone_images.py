from sqlalchemy.sql import text
from datetime import datetime

from app.models import CapstoneImage, db, environment, SCHEMA

def seed_capstone_images():
    images = [
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/67dc5b1c4b1a4dca89345c5fa31c9728.png",
                capstone_id=1,
                user_id=1,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/e0b43ded9b4942fd87b128e41caf59e7.png",
                capstone_id=1,
                user_id=1,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/861790cc702944f08e178066a410ca72.png",
                capstone_id=1,
                user_id=1,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/6c438bcb7a944ccdb322ced8af7b19d8.png",
                capstone_id=1,
                user_id=1,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/3a5818888ade4936b3cede0896bc204b.png",
                capstone_id=2,
                user_id=2,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/94ae1de4de41414da27a644f5bcce984.png",
                capstone_id=2,
                user_id=2,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/76cb882768164494875ca531297196a4.png",
                capstone_id=2,
                user_id=2,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/f806513b0ae340eba5233fe77a1ea7d5.jpg",
                capstone_id=2,
                user_id=2,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/7e4c516c57ad4ccab927e3062aeb0d94.png",
                capstone_id=3,
                user_id=3,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/0798c181736745ffab778715aafa00a0.png",
                capstone_id=3,
                user_id=3,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/2bda83932c3142d9be8beaf26fb840de.png",
                capstone_id=3,
                user_id=3,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/a499f8922b8348d2af8d8731caecbd6b.png",
                capstone_id=4,
                user_id=4,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/4278212dc3384b02b996961b95bb615f.png",
                capstone_id=4,
                user_id=4,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/b310ea72a69341f6a564f6607f39b1f6.png",
                capstone_id=5,
                user_id=5,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/11a036365f784577ade1237e85fa6d3f.png",
                capstone_id=5,
                user_id=5,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/70a3d185e8564cb08ec25235e7154c8b.png",
                capstone_id=5,
                user_id=5,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/7494b1035cff434b9b6d02a4762d5619.png",
                capstone_id=5,
                user_id=5,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/1ebc951da9a64290812963feac0b3c4d.png",
                capstone_id=5,
                user_id=5,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/a2305eabb17d4cdba1f2a5dc1c01da91.png",
                capstone_id=6,
                user_id=6,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/de76fc694f274e98aefe2846482f9859.png",
                capstone_id=6,
                user_id=6,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/6b893897089c46eba5c665daa64c9832.png",
                capstone_id=6,
                user_id=6,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/9fd717c36710413baa414c6d1b49b28c.jpg",
                capstone_id=6,
                user_id=6,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/565ace762a3b4551a977e3f67bd7b63f.png",
                capstone_id=7,
                user_id=7,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/e17eb69638f0451e81ee9a70043128c0.png",
                capstone_id=7,
                user_id=7,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/7597e9606a714e7c86f235b12e3c6b46.png",
                capstone_id=7,
                user_id=7,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/a2a5dd732c474247ac56d372ffd38888.png",
                capstone_id=7,
                user_id=7,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/488098a1da1745c58baa4dc6e6a01b7a.png",
                capstone_id=8,
                user_id=8,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/ba4d667272514515832680a9c6140bf0.png",
                capstone_id=8,
                user_id=8,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/b665f467cd24472e836236b05c4ac5db.png",
                capstone_id=8,
                user_id=8,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/4ab512851c234d07a6b1934e5d9c6575.png",
                capstone_id=8,
                user_id=8,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/e0c1eebe0c5e4a549bc89a79dfd55863.png",
                capstone_id=9,
                user_id=9,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/d82c5c7047e44bc2bd252f07115a110c.png",
                capstone_id=9,
                user_id=9,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/56a99b54342c4653b7a1a73bc58cb675.png",
                capstone_id=9,
                user_id=9,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/7851e4a720794eb0ad0573a68f21e216.png",
                capstone_id=9,
                user_id=9,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/7fdefdfdfd8a46bb969fe1e312b15eaf.png",
                capstone_id=10,
                user_id=10,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/135e3d896a4e401490aa797451c8a4f1.png",
                capstone_id=10,
                user_id=10,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/42b370cce0f0432ba8f1e95bf09f3974.png",
                capstone_id=10,
                user_id=10,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/bb175c0b670a4d20a2f81e6e309cf3a3.png",
                capstone_id=10,
                user_id=10,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/4b4ec9f65bcb41fb9db4328adeb1c9a3.png",
                capstone_id=10,
                user_id=10,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/ea7b1458d09545f58837fbb701ddb756.png",
                capstone_id=11,
                user_id=11,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/c5c5abf5a8914bcbad7275804658c127.png",
                capstone_id=11,
                user_id=11,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/44bf378f60b747d399833e70342149b9.png",
                capstone_id=11,
                user_id=11,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/d59264eed689485a84d6b6c3689b6f39.png",
                capstone_id=11,
                user_id=11,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/58816533b33248748f4776fbfd1644ef.png",
                capstone_id=11,
                user_id=11,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/fc26e297f038426d8d25b0888c1911fc.png",
                capstone_id=12,
                user_id=12,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/a0163223f5a0443e9e2776a363b746c0.png",
                capstone_id=12,
                user_id=12,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/a8ad8ced287740dc9ad79f6aa2c5c16e.png",
                capstone_id=12,
                user_id=12,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/8a9fd494692e4d4bb42c8daf032e92fb.png",
                capstone_id=13,
                user_id=13,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/3c94c5a59cfa47b5a9a48f6860051bc3.png",
                capstone_id=13,
                user_id=13,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/04b269fbeab24e25b39d7c26103225c3.png",
                capstone_id=13,
                user_id=13,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/6e31f182c6814f32a06c4cb312aa80f3.png",
                capstone_id=14,
                user_id=14,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/36c1b881549e40ddbd4458d2a983e6ee.png",
                capstone_id=14,
                user_id=14,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/87dd305d55f54709a9ae100db2ef4921.png",
                capstone_id=14,
                user_id=14,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/097f73aa294543e38f846023bdc41aa1.png",
                capstone_id=14,
                user_id=14,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/2c896e588de942318d84f5fef560ac28.png",
                capstone_id=14,
                user_id=14,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/252a08267ced48fdb9413ba90fdaaf43.png",
                capstone_id=15,
                user_id=15,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/67cf00a4c9ed40e89c45839f13e22fdd.png",
                capstone_id=15,
                user_id=15,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/eb25acd638354803923c819288ed590d.png",
                capstone_id=16,
                user_id=16,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/8db9665b53f144f681c48508ce1f6b25.png",
                capstone_id=16,
                user_id=16,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/f85b4ec5de954c459869240458ccb15e.png",
                capstone_id=16,
                user_id=16,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/eda013191e0748f48ab206ffc5b71a33.png",
                capstone_id=16,
                user_id=16,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/01e9b293fe8145589c21533574c07f98.png",
                capstone_id=16,
                user_id=16,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/8590aef96cd444d59020a1931783ca70.png",
                capstone_id=17,
                user_id=17,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/8383442bd132441ab650f14f424e5c08.png",
                capstone_id=17,
                user_id=17,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/edd1da57ee4f4a79adbc0aeffec3f7cd.png",
                capstone_id=17,
                user_id=17,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/97aa98ae5e8448108852977cb635d4cd.png",
                capstone_id=18,
                user_id=18,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/772c34b5ecb44a99a03531d99967e621.png",
                capstone_id=18,
                user_id=18,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/b5ebc33615d94fd380b39ed7bfd81c76.png",
                capstone_id=18,
                user_id=18,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/45ae4d6705a144dd84cb76ec4642221c.png",
                capstone_id=19,
                user_id=19,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/eb630429ab644f58a97a05e2b24ff31c.png",
                capstone_id=19,
                user_id=19,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/a5a6f4527df84cb3bc4092c60eb502f9.png",
                capstone_id=19,
                user_id=19,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/24456de23e9a491b88ffadacf94320ca.png",
                capstone_id=19,
                user_id=19,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/2f09571ff5634fb79a70dc0741e3564f.png",
                capstone_id=19,
                user_id=19,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/3722770863f047779493254a73b0d825.png",
                capstone_id=20,
                user_id=20,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/59f8cda1c91644fdb381cefec9113139.png",
                capstone_id=20,
                user_id=20,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/4596332af9a249558e2206d1d9d336be.png",
                capstone_id=20,
                user_id=20,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/55a57f07a86d4d45b8bde19b43b16907.png",
                capstone_id=20,
                user_id=20,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/288da37ea8824a91bb77e9d2b9c8c815.png",
                capstone_id=21,
                user_id=21,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/8b875bf8d7e7401886e4992f45c2e97b.png",
                capstone_id=21,
                user_id=21,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/bad060f4fd2840058911b0810793950d.png",
                capstone_id=21,
                user_id=21,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/2eabb5344ee7473c977fd439a496f0a3.png",
                capstone_id=21,
                user_id=21,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/b09ca4c6941d45e8beb3a2da497be251.png",
                capstone_id=21,
                user_id=21,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/3114234b297447dc87ec55e6f6b91e9d.gif",
                capstone_id=22,
                user_id=22,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/64750596465747e8b71edfa1fa8a3042.png",
                capstone_id=22,
                user_id=22,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/b222cf40bf824cf29f8769e325a8e974.png",
                capstone_id=22,
                user_id=22,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/e2e3c99f691947878c635942e8b05498.png",
                capstone_id=23,
                user_id=23,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/d7eee33d7dfd448dacd1a737b2a6bbe8.png",
                capstone_id=23,
                user_id=23,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/7cfa6147373c4f7db2084b7c409c0129.png",
                capstone_id=23,
                user_id=23,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/ae00dd5d7b374770b5944b04926b40d6.png",
                capstone_id=24,
                user_id=24,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/90c33515be284add88bafab5d5e12405.png",
                capstone_id=24,
                user_id=24,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/1bbc9bbe05b04a02909206ff930b7531.png",
                capstone_id=24,
                user_id=24,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/4c58fe0bdaca4c3f8543c6505c5450fd.png",
                capstone_id=25,
                user_id=25,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/013b245ef6dc4a2b8058005d6596a38f.png",
                capstone_id=25,
                user_id=25,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/2bdef22777b64477b33e6f4c4eaedf82.png",
                capstone_id=26,
                user_id=26,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/aaddacb7efe1429e8687fb59e9b3c519.png",
                capstone_id=26,
                user_id=26,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/ef4a5b5fefb2479cbbca90f13b253f6f.png",
                capstone_id=26,
                user_id=26,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/9ed6f86dca0c407fa78ca3a9c7c5e862.png",
                capstone_id=27,
                user_id=27,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/2c4c400fd3934bd7ae869e4819538ecc.png",
                capstone_id=27,
                user_id=27,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/23d3ae448d5b4ac3a38b5b5d486d1595.png",
                capstone_id=27,
                user_id=27,
                created_at=datetime.utcnow()
            ),
        CapstoneImage(
                image_url="https://captracker.s3.amazonaws.com/c201764406be49b99d468284db2a3d3c.jpg",
                capstone_id=27,
                user_id=27,
                created_at=datetime.utcnow()
            )
    ]

    db.session.commit()

def undo_capstone_images():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.capstoneimages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM capstoneimages"))

    db.session.commit()
