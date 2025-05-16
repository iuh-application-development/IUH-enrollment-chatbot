from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Major(Base):
    __tablename__ = 'major'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    code = Column(String(20))
    detail = Column(Text)

engine = create_engine('sqlite:///app.db')  # hoặc path phù hợp với project của bạn
Session = sessionmaker(bind=engine)
session = Session()

major_names = [
    "Ngành Công nghệ kỹ thuật máy tính",
    "Ngành Kiểm toán",
    "Ngành Luật quốc tế",
    "Ngành Thương mại điện tử",
    "Ngành Công nghệ kỹ thuật Cơ khí",
    "Ngành Công nghệ kỹ thuật điều khiển và tự động hóa",
    "Ngành Kỹ thuật công trình xây dựng",
    "Ngành Kỹ thuật xây dựng công trình giao thông",
    "Ngành Luật kinh tế",
    "Ngành Marketing",
    "Ngành Ngôn ngữ Anh",
    "Ngành Quản lý tài nguyên môi trường",
    "Ngành Công nghệ may",
    "Chuyên ngành Hóa phân tích",
    "Ngành Công nghệ kỹ thuật hóa học (02 chuyên ngành: Công nghệ kỹ thuật hóa học; Hóa phân tích)",
    "Ngành Kỹ thuật phần mềm",
    "Ngành Công nghệ thông tin",
    "Ngành Hệ thống thông tin",
    "Ngành Công nghệ kỹ thuật điện, điện tử",
    "Ngành Công nghệ chế tạo máy",
    "Ngành Công nghệ kỹ thuật nhiệt",
    "Ngành Công nghệ kỹ thuật điện tử viễn thông",
    "Ngành Khoa học máy tính",
    "Ngành Công nghệ kỹ thuật ôtô",
    "Ngành Công nghệ kỹ thuật cơ Điện tử",
    "Ngành Công nghệ thực phẩm",
    "Ngành Công nghệ sinh học",
    "Ngành Công nghệ kỹ thuật môi trường",
    "Ngành Quản trị kinh doanh (03 chuyên ngành: Quản trị kinh doanh; Quản trị nguồn nhân lực; Logistics và chuỗi cung ứng)",
    "Ngành Kinh doanh quốc tế",
    "Chuyên ngành quản trị khách sạn",
    "Ngành Quản trị dịch vụ du lịch và lữ hành (03 chuyên ngành: Quản trị dịch vụ du lịch lữ hành; Quản trị khách sạn; Quản trị nhà hàng và dịch vụ ăn uống)",
    "Chuyên ngành quản trị nhà hàng và dịch vụ ăn uống",
    "Ngành Tài chính ngân hàng (gồm 02 chuyên ngành: Tài chính ngân hàng; Tài chính doanh nghiệp)",
    "Chuyên ngành tài chính doanh nghiệp",
    "Ngành Kế toán",
    "Ngành Thương mại điện tử"
]

for name in major_names:
    session.add(Major(name=name, code="", detail=""))

session.commit()
print("✅ Đã thêm mặc định các ngành học.")

