from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float
from sqlalchemy import insert

def modeler(dates, data):
    engine = create_engine('sqlite:///D:/CODES/PROJECTS/MyAnimeList Data/mal_playwright/mal_db.db', echo= False)
    meta = MetaData()
    anime = Table(
        f'MAL_Data_{dates}', meta,
        Column('Title', String, unique=True),
        Column('Voters', Integer ),
        Column('Avg Score', Float ),
        Column('Year', Integer),
        Column('Season', String),
        Column('Studio', String),
        Column('Genre(s)', String),
        Column('Media', String),
        Column('Status', String),
        Column('Eps', String),
        Column('Duration(min)', Integer)
    )

    meta.create_all(engine)

    ins = insert(anime).prefix_with('OR IGNORE')  # This is similar to INSERT OR IGNORE in SQLite
    results = engine.execute(ins, data)
    

