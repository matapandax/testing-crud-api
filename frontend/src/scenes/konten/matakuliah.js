import * as React from 'react';
import { Box, Button, Typography, useTheme } from "@mui/material";
import { tokens } from "../../theme";
// import { mockTransactions } from "../../data/mockData";
// import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
// import EmailIcon from "@mui/icons-material/Email";
// import PointOfSaleIcon from "@mui/icons-material/PointOfSale";
// import PersonAddIcon from "@mui/icons-material/PersonAdd";
// import TrafficIcon from "@mui/icons-material/Traffic";
import Header from "../../components/Header";
// import LineChart from "../../components/LineChart";
// import GeographyChart from "../../components/GeographyChart";
import PieChart from "../../components/PieChart";
import BarChart from "../../components/XBarChart";
// import StatBox from "../../components/StatBox";
// import ProgressCircle from "../../components/ProgressCircle";
import { mockPieDataJenjang as dataJenjang } from "../../data/mockData";
import { mockPieDataSks as dataSks } from "../../data/mockData";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { mockDataContacts } from "../../data/mockData";

const styles = {
    instructor: {
        width: "450px",
        height: "150px",
        backgroundImage: "url('../../assets/matakuliah278.png')",
        backgroundRepeat: "no-repeat",
        backgroundSize: "contain",
        borderRadius: "15px",
        marginBottom: "15px"
    },
    self: {
        width: "450px",
        height: "150px",
        backgroundImage: "url('../../assets/matakuliah279.png')",
        backgroundRepeat: "no-repeat",
        backgroundSize: "contain",
        borderRadius: "15px"
    },
    container: {
        position: "relative",
        textAlign: "center",
    },
    text: {
        position: "absolute",
        width: "200px",
        top: "70%",
        left: "27%",
        transform: "translate(-50%, -50%)",
        fontSize: "64px",
        fontFamily: "Montserrat",
        fontStyle: "normal",
        fontWeight: "600",
        lineHeight: "96px",
    }
};

const columns = [
  { field: "id", headerName: "ID", flex: 0.5 },
  // { field: "registrarId", headerName: "Registrar ID" },
  {
    field: "name",
    headerName: "Nama Mata Kuliah",
    flex: 1,
    cellClassName: "name-column--cell",
  },
  {
    field: "city",
    headerName: "Institutsi Mata Kuliah",
    flex: 1,
  },
  {
    field: "detail",
    headerName: "Action",
    flex: 1,
  },
];


const Matakuliah = () => {
  const [open, setOpen] = React.useState(true);

  const handleOpen = () => {
    setOpen(!open);
  };
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <Box m="20px">
      {/* HEADER */}
      <Box display="flex" justifyContent="space-between" alignItems="center">
        <Header title="MATA KULIAH" subtitle="Dashboard mata kuliah ICE Institute" />

        <Box>
          <Button
            sx={{
              backgroundColor: colors.blueAccent[700],
              color: colors.grey[100],
              fontSize: "14px",
              fontWeight: "bold",
              padding: "10px 20px",
            }}
            onClick={handleOpen}
          >
            {/* <DownloadOutlinedIcon  sx={{ mr: "10px" }} /> */}
            {open ? <div>Semester</div>
            :
            <ul style={{listStyle: "none"}}>
            <li>1</li>
            <li>2</li>
            <li>3</li>
          </ul>}
          </Button>
        </Box>
      </Box>

      {/* GRID & CHARTS */}
      <Box
        display="grid"
        gridTemplateColumns="repeat(12, 1fr)"
        gridAutoRows="140px"
        gap="35px"
      >
        {/* ROW 1 */}
        <Box
          gridColumn="span 7"
          gridRow="span 2">

        </Box>
        <Box
          gridColumn="span 5"
          gridRow="span 2">
            <Box
            backgroundColor={colors.primary[400]}
            position="relative"
            alignItems="center"
            justifyContent="center"
            style={styles.instructor}
            >
                <div style={styles.text}>
                    <b>214</b>
                </div>
            </Box>
            <Box
            backgroundColor={colors.primary[400]}
            position="relative"
            alignItems="center"
            justifyContent="center"
            style={styles.self}
            >
                <div style={styles.text}>
                    <b>214</b>
                </div>
            </Box>
        </Box>
        {/* END ROW 1 */}
        
        {/* ROW 2 */}
        <Box
          gridColumn="span 4"
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
        >
          <Typography
            variant="h5"
            fontWeight="600"
            sx={{ padding: "30px 30px 0 30px" }}
          >
            Berdasarkan Bahasa
          </Typography>
          <Box height="250px" mt="-20px" pl="10px">
            <BarChart isDashboard={true} />
          </Box>
        </Box>
        <Box
          gridColumn="span 4"
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
        >
          <Typography
            variant="h5"
            fontWeight="600"
            sx={{ padding: "30px 30px 0 30px" }}
          >
            Berdasarkan Jenjang
          </Typography>
          <Box height="250px">
            <PieChart isDashboard={true} data= {dataJenjang} legendPos={{translateX:20, itemWidth: 80}}/>
          </Box>
        </Box>
        <Box
          gridColumn="span 4"
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
        >
          <Typography
            variant="h5"
            fontWeight="600"
            sx={{ padding: "30px 30px 0 30px" }}
          >
            Pesebaran Peserta
          </Typography>
          <Box height="250px">
            <PieChart isDashboard={true} data= {dataSks} legendPos={{translateX:20, itemWidth: 80}}/>
          </Box>
        </Box>
        {/* END ROW 2 */}
        
        {/* ROW 3 */}
        <Box
          gridColumn="span 4"
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
        >
          <Typography
            variant="h5"
            fontWeight="600"
            sx={{ padding: "30px 30px 0 30px" }}
          >
            Berdasarkan Bahasa
          </Typography>
          <Box height="250px" mt="-20px" pl="10px">
            <BarChart isDashboard={true} />
          </Box>
        </Box>
        <Box
          gridColumn="span 8"
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
        >
          <Typography
            variant="h5"
            fontWeight="600"
            sx={{ padding: "30px 30px 0 30px" }}
          >
            Berdasarkan Jenjang
          </Typography>
          <Box height="250px">
            <Box
              m="40px 0 0 0"
              height="75vh"
              sx={{
                "& .MuiDataGrid-root": {
                  border: "none",
                },
                "& .MuiDataGrid-cell": {
                  borderBottom: "none",
                },
                "& .name-column--cell": {
                  color: colors.greenAccent[300],
                },
                "& .MuiDataGrid-columnHeaders": {
                  backgroundColor: colors.blueAccent[700],
                  borderBottom: "none",
                },
                "& .MuiDataGrid-virtualScroller": {
                  backgroundColor: colors.primary[400],
                },
                "& .MuiDataGrid-footerContainer": {
                  borderTop: "none",
                  backgroundColor: colors.blueAccent[700],
                },
                "& .MuiCheckbox-root": {
                  color: `${colors.greenAccent[200]} !important`,
                },
                "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
                  color: `${colors.grey[100]} !important`,
                },
              }}
            >
              <DataGrid
                rows={mockDataContacts}
                columns={columns}
                components={{ Toolbar: GridToolbar }}
              />
            </Box>
          </Box>
        </Box>
        {/* END ROW 3 */}
      </Box>
    </Box>
  );
};

export default Matakuliah;
