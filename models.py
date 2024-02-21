from sqlalchemy import Column, Integer, Float, String, func
from sqlalchemy.ext.declarative import declarative_base
from database import get_db
import pandas as pd
import streamlit as st
from sqlalchemy.sql import desc



Base = declarative_base()

class IPL(Base):
     __tablename__ = 'ipl23'

     id = Column(Integer, primary_key=True)
     match_no = Column(Integer)
     ballnumber = Column(Integer)
     inningno = Column(Integer)
     over = Column(Float)
     outcome = Column(Integer)
     batter = Column(String)
     bowler = Column(String)
     comment = Column(String)
     score = Column(Integer)


     def get_data():
          db = next(get_db())
          data = []
          try:
               db = next(get_db())
               ipl_records = db.query(IPL).all()
               return ipl_records
          finally:
               db.close()
     
     def head_to_head():
          db = next(get_db())
          try:
               bowlers = db.query(IPL.bowler).all()
               batters = db.query(IPL.batter).all()
               bowler_df = pd.DataFrame(bowlers)
               batter_df = pd.DataFrame(batters)
               bowler_options = bowler_df['bowler'].unique()
               batter_option = batter_df['batter'].unique()
               bowler = st.selectbox("select bowler ", bowler_options)
               batter = st.selectbox("select batter", batter_option)
               query = db.query(
                    IPL.batter,
                    IPL.bowler,
                    # IPL.inningno,
                    func.sum(IPL.score).label('total_score'),
                    func.count(IPL.ballnumber).label('ball_faced')
               ).filter(
                    IPL.bowler == bowler,
                    IPL.batter == batter
               ).group_by(
                    IPL.batter,
                    IPL.bowler,
                    # IPL.inningno
               ).order_by(
                    desc('total_score')
               ).all()
               return query
          finally:
               db.close()
#     def __repr__(self):
#         return f"<Ball(match_no={self.match_no}, ballnumber={self.ballnumber}, inningno={self.inningno}, over={self.over}, outcome={self.outcome}, batter='{self.batter}', bowler='{self.bowler}', comment='{self.comment}', score={self.score})>"
     