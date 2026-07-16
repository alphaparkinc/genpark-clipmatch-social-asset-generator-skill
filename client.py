class ClipMatchSocialAssetGeneratorClient:
    def generate_timeline(self, raw_clips_meta: list[dict], vibe_theme: str) -> dict:
        # Simple heuristic filtering
        selected = [clip for clip in raw_clips_meta if clip.get("duration", 0) > 2.0][:3]
        genre = "Lo-Fi" if vibe_theme == "chill" else "Synthwave" if vibe_theme == "retro" else "Pop"
        return {"selected_timeline": selected, "music_genre": genre}