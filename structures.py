from pydantic import BaseModel


class Image(BaseModel):
    displayed: bool
    path: str


class Media_data(BaseModel):
    image: Image
    video_before: str
    video_after: str


class Tactics(BaseModel):
    remove_answer: int
    one_for_all: int
    question_bet: int
    all_in: int
    team_bet: int


class Questions(BaseModel):
    type: str
    question: str
    answers: str | list[str] = None
    correct_answer: str | int | list[int] = None
    time_to_answer: int = None
    media_data: Media_data = None


class Settings(BaseModel):
    is_test: bool
    name: str
    display_name: bool
    time_to_answer: int
    use_special_tactics: bool = None
    tactics: Tactics = None


class Rounds(BaseModel):
    type: str
    settings: Settings
    questions: list[Questions]


class Game_settings(BaseModel):
    tactics: Tactics


class Game(BaseModel):
    game_settings: Game_settings
    name: str
    rounds: list[Rounds]
