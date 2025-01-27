import dataclasses


@dataclasses.dataclass
class ExcelOPR:
    pos_num: str
    opr_date: str
    request_type: str
    sup_div: str
    physical_location: str
    state: str
    supply_geo_cluster: str
    supply_geo_reg: str
    supply_ctry: str
    level: str
    position_title: str
    service_description: str
    contract_type: str
    sup_fun_area: str
    sup_dept: str
    sup_res_area: str
    sup_res_sarea: str
    jnj_sponsor_wwid: str
    jnj_sponsor_name: str
    email: str
    target_start_date: str
    cost_center: str

    def __init__(
            self, pos_num, opr_date, request_type, sup_div, physical_location, state, supply_geo_cluster,
            supply_geo_reg, supply_ctry, level, position_title, service_description, contract_type, sup_fun_area,
            sup_dept, sup_res_area, sup_res_sarea, jnj_sponsor_wwid, jnj_sponsor_name, email, target_start_date,
            cost_center):
        self.pos_num = pos_num
        self.opr_date = opr_date
        self.request_type = request_type
        self.sup_div = sup_div
        self.physical_location = physical_location
        self.state = state
        self.supply_geo_cluster = supply_geo_cluster
        self.supply_geo_reg = supply_geo_reg
        self.supply_ctry = supply_ctry
        self.level = level
        self.position_title = position_title
        self.service_description = service_description
        self.contract_type = contract_type
        self.sup_fun_area = sup_fun_area
        self.sup_dept = sup_dept
        self.sup_res_area = sup_res_area
        self.sup_res_sarea = sup_res_sarea
        self.jnj_sponsor_wwid = jnj_sponsor_wwid
        self.jnj_sponsor_name = jnj_sponsor_name
        self.email = email
        self.target_start_date = target_start_date
        self.cost_center = cost_center

    @classmethod
    def header(cls):
        # Keys: POS #,OPR DATE,REQUEST TYPE,SUP DIV,PHYSICAL LOCATION,STATE (PHYSICAL LOCATION),SUPPLY GEO CLUSTER,
        # SUPPLY GEO REG,SUPPLY CTRY,LEVEL,POSITION TITLE (DERIVED),SERVICE DESCRIPTION,CONTRACT TYPE,SUP FUN AREA,
        # SUP DEPT,SUP RES AREA,SUP RES SAREA,J&J SPONSOR WWID,J&J SPONSOR NAME,EMAIL,TARGET START DATE,COST CENTER
        return [
            "POS #", "OPR DATE", "REQUEST TYPE", "SUP DIV", "PHYSICAL LOCATION", "STATE (PHYSICAL LOCATION)",
            "SUPPLY GEO CLUSTER", "SUPPLY GEO REG", "SUPPLY CTRY", "LEVEL", "POSITION TITLE (DERIVED)",
            "SERVICE DESCRIPTION", "CONTRACT TYPE", "SUP FUN AREA", "SUP DEPT", "SUP RES AREA", "SUP RES SAREA",
            "J&J SPONSOR WWID", "J&J SPONSOR NAME", "EMAIL", "TARGET START DATE", "COST CENTER"
        ]


@dataclasses.dataclass
class ExcelComments(ExcelOPR):
    icon_status: str
    iqvia_comments: str

    @classmethod
    def header(cls):
        # IQVIA's Comments,ICON STATUS (Manager Review)
        return super().header() + ["ICON STATUS (Manager Review)", "IQVIA's Comments"]


@dataclasses.dataclass
class ExcelIQVIA(ExcelComments):
    def __init__(self, *args):
        super().__init__(*args[:-1], iqvia_comments=args[-1], icon_status="")


@dataclasses.dataclass
class ExcelICON(ExcelComments):
    def __init__(self, *args):
        super().__init__(*args[:2], *args[3:], iqvia_comments="", icon_status=args[2])
