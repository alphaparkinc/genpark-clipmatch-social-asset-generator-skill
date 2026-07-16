from client import ClipMatchSocialAssetGeneratorClient
client = ClipMatchSocialAssetGeneratorClient()
print(client.generate_timeline([{"id": 1, "duration": 4.5}, {"id": 2, "duration": 1.2}], "chill"))